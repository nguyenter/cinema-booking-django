# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_movie_ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Mã suất chiếu')),
                ('start_time', models.DateTimeField(verbose_name='Thời gian bắt đầu')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Thời gian kết thúc')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang hoạt động')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='book_movie_ticket_app.movie', verbose_name='Phim')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_movie_ticket_app.room', verbose_name='Phòng chiếu')),
            ],
            options={
                'verbose_name': 'Suất chiếu',
                'verbose_name_plural': 'Suất chiếu',
                'ordering': ['start_time'],
                'unique_together': {('movie', 'room', 'start_time')},
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='showtime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book_movie_ticket_app.showtime', verbose_name='Suất chiếu'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_time',
            field=models.DateTimeField(blank=True, help_text='Giữ lại để tương thích với dữ liệu cũ', null=True, verbose_name='Ngày giờ chiếu'),
        ),
    ]

