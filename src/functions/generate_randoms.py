from numpy import random as np_rand

class generate_randoms(object):
    # 构造说明
    # 1 传入分布类型和参数
    # 2 检查分布的参数是够符合要求，generate_randoms._check_distri_paras
    # 3 根据需求随机数个数生成随机数，以list格式传出 rands = generate_randoms.generating()

    #传入参数
    def __init__(self, distri, location_para=None, scale_para=None, shape_para=None, number_rand=10):
        #只可选均匀分布、指数分布、正态分布、对数正态分布、威布尔分布
        #对应'uniform_distri','exponential_distri','normal_distri','lognormal_distri','weibull_distri'
        self.distri = distri 
        #一个分布至少有一个参数，即位置参数、尺度参数或形状参数
        self.location_para = location_para #位置参数
        self.scale_para = scale_para #尺度参数，比例参数
        self.shape_para = shape_para #形状参数
        self.number_rand = number_rand #生成随机数个数，默认为10个随机数

    #检查参数是否与分布对应合理
    def _check_distri_paras(self):
        check = False
        #均匀分布
        if self.distri=='uniform_distri':
            if (self.location_para != None) and (self.scale_para != None):
                check = True
        #指数分布
        elif self.distri=='exponential_distri':
            if self.scale_para != None:
                check = True
        #正态分布
        elif self.distri=='normal_distri':
            if (self.location_para != None) and (self.scale_para != None):
                check = True
        #对数正态分布
        elif self.distri=='lognormal_distri':
            if (self.scale_para != None) and (self.shape_para != None):
                check = True
        #威布尔分布
        elif self.distri=='weibull_distri':
            if (self.scale_para != None) and (self.shape_para != None):
                check = True
        return check
    #生成随机数
    def generating(self):
        if self._check_distri_paras() :
            #均匀分布
            if self.distri=='uniform_distri':
                rands = np_rand.uniform(low=self.location_para, 
                                        high=(self.location_para+self.scale_para), 
                                        size=self.number_rand).tolist()
            #指数分布
            elif self.distri=='exponential_distri':
                rands = np_rand.exponential(scale=self.scale_para, size=self.number_rand).tolist()
            #正态分布
            elif self.distri=='normal_distri':
                rands = np_rand.normal(loc=self.location_para, scale=self.scale_para, size=self.number_rand).tolist()
            #对数正态分布
            elif self.distri=='lognormal_distri':
                rands = np_rand.lognormal(mean=self.scale_para, sigma=self.shape_para, size=self.number_rand).tolist()
            #威布尔分布
            elif self.distri=='weibull_distri':
                rands = np_rand.weibull(a=self.shape_para, size=self.number_rand)
                rands = rands * self.scale_para
                rands = rands.tolist()
        else:
            print('PDF函数的参数设置不正确')
        
        return rands