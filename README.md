**# Product Sales Prediction API

Bu proje, Northwind veritabanını kullanarak ürün satış tahminleri yapmak amacıyla geliştirilmiştir. FastAPI framework'ü kullanılarak bir REST API oluşturulmuş ve scikit-learn kütüphanesiyle makine öğrenmesi modeli eğitilmiştir.

##  Proje Özeti

Bu API, verilen ürün ID'sine ve çeşitli ürün özelliklerine (fiyat, stok miktarı, yeniden sipariş seviyesi) göre tahmini satış miktarını döner. Model eğitimi için veritabanındaki satış verileri kullanılmıştır.


##  Kullanılan Teknolojiler

- Python
- FastAPI
- SQLAlchemy
- Pandas
- NumPy
- scikit-learn
- PostgreSQL


##  Proje Dosya Yapısı

```
├── main.py              
├── requirements.txt     
├── README.md  
```


##  Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. PostgreSQL sunucunuzda Northwind veritabanını oluşturun ve uygun tabloları ekleyin.

3. `DATABASE_URL` bağlantı dizesini kendi veritabanınıza göre düzenleyin.


##  API Kullanımı

API'yi çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
```bash
uvicorn main:app --reload
```

###  API Dökümantasyonu

API dökümantasyonuna erişmek için:
- Tarayıcınızdan şu adrese gidin: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)
- Alternatif olarak: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (ReDoc)

Bu sayfalar üzerinden API'yi test edebilir ve dökümantasyonu inceleyebilirsiniz.

###  Postman Koleksiyonu
Postman üzerinden API'yi test etmek isterseniz, [Product_Sales_Prediction_API.postman_collection.json](./docs/Product_Sales_Prediction_API.postman_collection.json) dosyasını import edebilirsiniz.
     

### POST /predict/
**Request Body:**

![Request Body](./BiP%20image%202025-04-02%20pmt%2021.32.17.jpg)

**Response:**

![Response](./BiP%20image%202025-04-02%20pmt%2021.32.14.jpg)

## Model Performansı

Model eğitimi sırasında aşağıdaki metrikler hesaplanmıştır:

- **Root Mean Squared Error (RMSE):** 349.43634513800134
- **R-squared:** -0.11801155941127073

## Katkı Sağlayanlar 

Bu proje aşağıdaki kişiler tarafından gerçekleştirilmiştir:

- **Özge Solmaz** - (solmazozge02@gmail.com)
- **Nisasu Bozkurt** - (nisasubozkurt@gmail.com)
- **Zeynep Vural** - (zeynebvural450@gmail.com)
- **Gülizar Tuncer** - (Rgulizartuncer@gmail.com)
- **İrem Zorbaz Özün** - (irm.zrbzz@gmail.com)**

















  
