"""
Fonksiyonun çalışma prensibi:

1. Her bir sütunun sol ve sağ tarafındaki en yüksek sütunları belirleriz, 
   çünkü suyun birikmesi için o sütunun iki tarafında yüksek sütunlar olması gerekir.

2. Her sütunun su tutma kapasitesi, sol ve sağ tarafındaki en yüksek sütunların 
   minimum yüksekliği ile belirlenir. Bu minimum değerden mevcut sütun yüksekliğini 
   çıkardığımızda, o sütunda biriken su miktarını buluruz.

3. Tüm sütunlardaki su miktarını toplayarak toplam su hacmini elde ederiz.


"""

def calcWaterArea(heights):
    # sütunların sayısını al
    n = len(heights)
    
    # Eğer boşsa
    if n == 0:
        return 0
    
    left_max = [0] * n  # soldan en yüksek değer
    right_max = [0] * n  # sağdan en yüksek değer
    
    # soldan sağa maksimum yükseklikleri ekle
    left_max[0] = heights[0] 
    for i in range(1, n): # son eleman
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # sağdan sola maksimum yükseklikleri ekle
    right_max[n - 1] = heights[n - 1]  #son eleman
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # Toplam su miktarını hesaplama partı
    total_water = 0
    for i in range(n):
        """
         Her sütunun tutabileceği su miktarı, sol ve sağdaki maksimum yüksekliklerin minimum değeri ile belirlenir
         Mevcut yüksekliği bu değerden çıkararak su miktarını bulduk
        """
        water_at_i = min(left_max[i], right_max[i]) - heights[i]
        
        # su miktarı negatifse sıfır al
        if water_at_i > 0:
            total_water += water_at_i 
    
    return total_water  


heights = eval(input("Sütun yüksekliklerini girin (örn [1,2,....]):"))
result = calcWaterArea(heights)
print(f"Toplam su miktarı: {result} m3")