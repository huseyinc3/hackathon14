# EVALTS

EVALTS, kullanıcıların IELTS Writing performanslarını değerlendirmek ve zaman içindeki gelişimlerini takip edebilmek için geliştirilen yapay zeka destekli bir uygulamadır. Kullanıcıdan bir ID alınarak her yazı için AI tarafından bant skoru değerlendirmesi yapılır ve bu skorlar veritabanına kaydedilir. Aynı ID ile tekrar giriş yapan kullanıcılar, önceki skorlarına göre oluşturulan gelişim grafiğini görüntüleyebilir. Uygulamada doğal dil işleme (NLP) tabanlı yapay zeka teknolojileri kullanılmıştır.
## Özellikler

- IELTS Task 1 ve Task 2 değerlendirmesi
- TOEFL Writing değerlendirmesi
- Band skoru ve grafik analizi
- Yazım hatalarını bulma ve düzeltme
- Essay geliştirme önerileri
- Kullanıcıya özel geçmiş kaydı

⚠️ Not: Bu uygulama Google Gemini 1.5 Pro API'si kullanmaktadır. Ücretsiz kullanım kotası günlük 50 sorgu ile sınırlıdır. Kota dolduğunda değerlendirme fonksiyonları geçici olarak çalışmaz. Lütfen ertesi gün yeniden deneyin.

⚠️ Not: Projenin ilerleme takibinin yapılabilmesi için commit kısmına değil linkteki repolara bakılmasını arz ederiz. Tek repo üzerinde çalışamadık. https://github.com/Dilara263/WriteEval,

https://github.com/huseyinc3/EVALTS,

https://github.com/huseyinc3/WriteEval.

## Kurulum

```bash
git clone https://github.com/huseyinc3/EVALTS.git
cd WriteEval
pip install -r requirements.txt
