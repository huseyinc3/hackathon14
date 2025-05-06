from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import pytz

# SQLAlchemy base sınıfı
Base = declarative_base()

# Türkiye saat dilimi
turkey_tz = pytz.timezone("Europe/Istanbul")

# Feedback modeli
class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    essay_text = Column(String)
    task_type = Column(String)
    band_task = Column(Float)
    band_coherence = Column(Float)
    band_lexical = Column(Float)
    band_grammar = Column(Float)
    band_overall = Column(Float)
    evaluation_text = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(tz=turkey_tz))  # UTC+3

# Veritabanı bağlantısı ve session ayarı
engine = create_engine("sqlite:///feedbacks.db", connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
