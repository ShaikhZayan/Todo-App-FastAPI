from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://ShaikhZayan:1FH4LoSaOtDn@ep-shiny-mode-a5u1uzk7.us-east-2.aws.neon.tech/todo?sslmode=require', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
