from django.contrib import admin
from apps.screen.models import Screen
from apps.seat.models import Seat



map = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
    5 : "E",
    6 : "F",
    7 : "G",
    8 : "H",
    9 : "I",
    10 : "J",
    11 : "K",
    12 : "L",
    13 : "M",
    14 : "N",
    15 : "O",
    16 : "P",
    17 : "Q",
    18 : "R",
    19 : "S",
    20 : "T",
    21 : "U",
    22 : "V",
    23 : "W",
    24 : "X",
    25 : "Y",
    26 : "Z",
}

# Register your models here.
@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'is_available' , 'rows' , 'columns' , 'total_capacity']

    def save_model(self, request, obj, form, change):
        if change is False : 
            
            for row in range(obj.rows):
                for col in range(obj.columns):
                    Seat.objects.create(
                        seat_number = f"{map[row+1]}{col+1}-{obj.name}",
                        row = row+1,
                        column = col+1,
                        screen = obj,
                    )
        super().save_model(request, obj, form, change)        
                    
