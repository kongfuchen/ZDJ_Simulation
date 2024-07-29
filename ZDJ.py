class ZDJ(object):
    def __init__(self) :
        self.zdj_cbs=0#折叠机出包数量
        self.zdj_cbs_list = [] #各长条折叠出包时刻
        self.paperLength_list=[]#剩余米数
        self.DATA_LIST_ZJ_RBS = [] #各长条折叠入包时刻

def product_ctzd(env,zdj,INITIAL_LENGTH,ZDJ_SPEED_STYLE,TIME_One_DZ,TIME_SPEED_CHANGE,SPEED_CHANGE,NO_OF_SHEETS,LENGTH_OF_SHEETS,TIME_ZD_MOVE):
    
    
    product_time=0#折叠机生产时间
    SAMPLING_TIME=0.2#采样时间
    NO_OF_ctzd=0#折叠机生产的长条纸叠数量
    
    zj_length=0#处理的原纸长度
    current_speed=0#折叠机的当前速度
    
    while True:
        if ZDJ_SPEED_STYLE == 0:
            yield env.timeout(SAMPLING_TIME)
            product_time=product_time+SAMPLING_TIME
            zj_length = zj_length + (NO_OF_SHEETS*LENGTH_OF_SHEETS/2)*(SAMPLING_TIME/TIME_One_DZ)
            paper_change(INITIAL_LENGTH,zj_length,env,zdj)
            if(product_time-TIME_One_DZ*NO_OF_ctzd>=TIME_One_DZ):
                NO_OF_ctzd = NO_OF_ctzd + 1
                zdj.DATA_LIST_ZJ_RBS.append([env.now,NO_OF_ctzd])
                env.process(convey(NO_OF_ctzd,zdj,env,TIME_ZD_MOVE)) #czj,
        else:
            for i in range(len(TIME_SPEED_CHANGE)):#确定速度
                if env.now>=TIME_SPEED_CHANGE[len(TIME_SPEED_CHANGE)-1]:
                    current_speed=SPEED_CHANGE[len(TIME_SPEED_CHANGE)-1]
                    break
                elif env.now>=TIME_SPEED_CHANGE[i] and env.now<TIME_SPEED_CHANGE[i+1]:
                    current_speed=SPEED_CHANGE[i]
                    break
            yield env.timeout(SAMPLING_TIME)
            #生产长条纸叠
            if current_speed>=0:
                zj_length=zj_length+current_speed*SAMPLING_TIME
                
                paper_change(INITIAL_LENGTH,zj_length,env,zdj)

                if  ((zj_length-NO_OF_ctzd*NO_OF_SHEETS*LENGTH_OF_SHEETS/2)/(NO_OF_SHEETS*LENGTH_OF_SHEETS/2))>=1:
                    NO_OF_ctzd=NO_OF_ctzd+1                        
                    zdj.DATA_LIST_ZJ_RBS.append([env.now,NO_OF_ctzd])                   
                    env.process(convey(NO_OF_ctzd,zdj,env,TIME_ZD_MOVE)) 
                                         
def convey(no_of_rbs,zdj,env,TIME_ZD_MOVE):    
    yield env.timeout(TIME_ZD_MOVE)                
    zdj.zdj_cbs=no_of_rbs                        
    zdj.zdj_cbs_list.append([env.now,zdj.zdj_cbs])             
def paper_change(ini_length,zj_length,env,zdj):    
    paper_length=[]
    for i in range(len(ini_length)):
        if ini_length[i]>10:
            paper_length.append(ini_length[i]-zj_length*0.983)
        else :
            paper_length.append(ini_length[i])
    zdj.paperLength_list.append([env.now,paper_length])
  





                        
                


            
            
            
            
        

