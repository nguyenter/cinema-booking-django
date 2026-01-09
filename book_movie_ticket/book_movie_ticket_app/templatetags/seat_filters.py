from django import template

register = template.Library()

@register.filter
def get_seat_label(seat_index, seats_per_row=15):
    """Convert seat index to format like A1, A2, A3...A15, B1, B2..."""
    row = seat_index // seats_per_row
    col = seat_index % seats_per_row
    row_letter = chr(65 + row)  # A=65, B=66, C=67...
    col_number = col + 1  # Columns start from 1
    return f"{row_letter}{col_number}"

@register.filter
def get_row_class(seat_index, seats_per_row=15):
    """Get CSS class for row (green for A-D, red for E-K)"""
    row = seat_index // seats_per_row
    if row < 4:  # Rows A-D (0-3)
        return "row-green"
    else:  # Rows E and above (4+)
        return "row-red"
