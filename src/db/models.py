from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    is_admin = Column(Boolean, default=False)  # 是否 管理员

    def __str__(self):
        return '<User: {}, {}>'.format(self.id, self.name)


class SimModel(Base):
    __tablename__ = 'input_file'  # 三维模型表

    id = Column(Integer, primary_key=True)  # 编号
    name = Column(String(100), nullable=True)  # 模型名称
    jnl_path = Column(String(500), nullable=False)  # 模型由abaqus生成的jnl文件
    external_model_path = Column(String(500), nullable=True)  # 如果jnl文件的模型时外部导入的，需要其路径

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('sim_models', cascade="all,delete"))


class Param(Base):
    __tablename__ = 'input_paras'  # 环境参数表

    id = Column(Integer, primary_key=True)  # 编号
    name = Column(String(100), nullable=False)  # 载荷类型(名称)
    distri = Column(String(40), nullable=False)  # 载荷服从分布
    location_para = Column(Float, nullable=True)  # 位置参数
    scale_para = Column(Float, nullable=True)  # 比例参数
    shape_para = Column(Float, nullable=True)  # 形状参数
    unit = Column(String(40), nullable=False)  # 载荷的单位

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('params', cascade="all,delete"))
