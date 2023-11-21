from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float



user = 'root'
password = 'Kouki2522'
host = 'localhost'
db_name = 'samplefastAPI'

# engineの設定
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}')


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# テーブルを作成する
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Base.query  = db_session.query_property()
# # テーブルを定義する
# # Baseを継承
# class Wine(Base):
#   """ワインの情報をもつCSVファイルのクラス

#   Args:
#       Base (_type_): DeclarativeBase
#   """
#   # テーブル名
#   __tablename__ = 'wines'
#   # カラムの定義
#   id = Column(Integer, primary_key=True, autoincrement=True)
#   wine_class = Column(Integer, unique=False)
#   alcohol = Column(Float, unique=False)
#   ash = Column(Float, unique=False)
#   hue = Column(Float, unique=False)
#   proline = Column(Integer, unique=False)
  
#   def __init__(self, wine_class=None, alcohol=None, ash=None, hue=None, proline=None):
#     self.wine_class = wine_class
#     self.alcohol = alcohol
#     self.ash = ash
#     self.hue = hue
#     self.proline = proline

# Base.metadata.create_all(bind=engine)

# def read_data():
#   """CSVファイルを読み込み、DBにデータを追加する関数
#   """
#   wine_df = pd.read_csv('./data/wine_class.csv')

#   for index, _df in wine_df.iterrows():
#     row = Wine(wine_class=_df['Class'], alcohol=_df['Alcohol'], ash=_df['Ash'], hue=_df['Hue'], proline=_df['Proline'])
#     # データを追加する
#     db_session.add(row)

#   db_session.commit()

# read_data()
