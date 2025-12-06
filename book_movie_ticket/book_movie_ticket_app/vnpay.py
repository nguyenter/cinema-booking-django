"""
VNPay Payment Gateway Integration
Based on VNPay official documentation
"""
import hmac
import hashlib
from urllib.parse import quote_plus, urlencode
from django.conf import settings


class vnpay:
    requestData = {}
    responseData = {}

    def get_payment_url(self, vnpay_payment_url, secret_key):
        # Loại bỏ các giá trị rỗng và None
        inputData = {}
        for key, val in self.requestData.items():
            if val is not None and val != '':
                inputData[key] = str(val)
        
        # Sắp xếp theo thứ tự alphabet (theo key)
        sorted_data = sorted(inputData.items())
        
        # Tạo query string để tính hash (KHÔNG encode, KHÔNG bao gồm SecureHash và SecureHashType)
        # Format: key1=value1&key2=value2&...
        queryString = ''
        seq = 0
        for key, val in sorted_data:
            if seq == 1:
                queryString += '&' + key + '=' + str(val)
            else:
                seq = 1
                queryString = key + '=' + str(val)
        
        # Debug: In ra query string để tính hash
        print("=" * 60)
        print("Query String for Hash Calculation:")
        print(queryString)
        print("=" * 60)
        
        # Tính hash từ query string (chưa encode)
        hashValue = self.__hmacsha512(secret_key, queryString)
        
        print("Calculated Hash:", hashValue)
        print("=" * 60)
        
        # Thêm SecureHashType và SecureHash vào inputData
        inputData['vnp_SecureHashType'] = 'SHA512'
        inputData['vnp_SecureHash'] = hashValue
        
        # Sắp xếp lại để tạo URL cuối cùng (bao gồm cả hash)
        sorted_final = sorted(inputData.items())
        
        # Tạo query string cuối cùng (có encode URL)
        queryString_final = ''
        seq = 0
        for key, val in sorted_final:
            # Encode giá trị cho URL
            encoded_val = quote_plus(str(val))
            
            if seq == 1:
                queryString_final += '&' + key + '=' + encoded_val
            else:
                seq = 1
                queryString_final = key + '=' + encoded_val
        
        print("Final Payment URL (first 300 chars):")
        final_url = vnpay_payment_url + "?" + queryString_final
        print(final_url[:300] + "..." if len(final_url) > 300 else final_url)
        print("=" * 60)
        
        return final_url

    def validate_response(self, vnp_Params, secret_key):
        vnp_SecureHash = vnp_Params.get('vnp_SecureHash', '')
        if not vnp_SecureHash:
            print("Validate Response: No vnp_SecureHash found")
            return False
            
        # Remove hash from params để tính lại hash
        vnp_Params_copy = vnp_Params.copy()
        if 'vnp_SecureHash' in vnp_Params_copy:
            vnp_Params_copy.pop('vnp_SecureHash')
        if 'vnp_SecureHashType' in vnp_Params_copy:
            vnp_Params_copy.pop('vnp_SecureHashType')

        # Sắp xếp và tạo query string (chưa encode để tính hash)
        inputData = sorted(vnp_Params_copy.items())
        hasData = ''
        seq = 0
        for key, val in inputData:
            if seq == 1:
                hasData += '&' + key + '=' + str(val)
            else:
                seq = 1
                hasData = key + '=' + str(val)

        print(f"Validate Response - Query String for Hash: {hasData}")
        hashValue = self.__hmacsha512(secret_key, hasData)
        print(f"Validate Response - Received Hash: {vnp_SecureHash}")
        print(f"Validate Response - Calculated Hash: {hashValue}")
        print(f"Validate Response - Match: {vnp_SecureHash == hashValue}")

        return vnp_SecureHash == hashValue

    def __hmacsha512(self, key, data):
        byteKey = key.encode('utf-8')
        byteData = data.encode('utf-8')
        return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()
