class ZDJ(object):
    def __init__(self) :
        self.zdj_cbs=0#折叠机出包数量
        self.zdj_cbs_list = [] #各长条折叠出包时刻
        self.zdj_rbs_trans='0'#用于回传仿真结果的折叠机入包数量
        self.zdj_cbs_trans='0'#用于回传仿真结果的折叠机出包数量
        self.paperLength_list=[]#剩余米数
        self.DATA_LIST_ZJ_RBS = [] #各长条折叠入包时刻
        self.num_record_rbs=1#用于回传仿真结果的折叠机入包数量的计数
        self.num_record_cbs=1#用于回传仿真结果的折叠机出包数量的计数
        self.num_record_syms=1#用于回传仿真结果的剩余米数的计数

def product_ctzd(env,zdj,INITIAL_LENGTH,ZDJ_SPEED_STYLE,TIME_One_DZ,TIME_SPEED_CHANGE,SPEED_CHANGE,NO_OF_SHEETS,LENGTH_OF_SHEETS,TIME_ZD_MOVE,return_time_interval):
    
    
    product_time=0#折叠机生产时间
    SAMPLING_TIME=0.2#采样时间
    NO_OF_ctzd=0#折叠机生产的长条纸叠数量
    
    zj_length=0#处理的原纸长度
    current_speed=0#折叠机的当前速度
    # zdj.paperLength_list = INITIAL_LENGTH
    for i in range(len(INITIAL_LENGTH)):
        zdj.paperLength_list.append(str(INITIAL_LENGTH[i]))
    
    while True:
        if ZDJ_SPEED_STYLE == 0:
            yield env.timeout(SAMPLING_TIME)
            product_time=product_time+SAMPLING_TIME
            zj_length = zj_length + (NO_OF_SHEETS*LENGTH_OF_SHEETS/2)*(SAMPLING_TIME/TIME_One_DZ)
            if(product_time-TIME_One_DZ*NO_OF_ctzd>=TIME_One_DZ):
                NO_OF_ctzd = NO_OF_ctzd + 1
                zdj.DATA_LIST_ZJ_RBS.append([env.now,NO_OF_ctzd])
                env.process(convey(NO_OF_ctzd,zdj,env,TIME_ZD_MOVE)) #czj,
            # paper_change(INITIAL_LENGTH,zj_length,env,zdj)
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
                if  ((zj_length-NO_OF_ctzd*NO_OF_SHEETS*LENGTH_OF_SHEETS/2)/(NO_OF_SHEETS*LENGTH_OF_SHEETS/2))>=1:
                    NO_OF_ctzd=NO_OF_ctzd+1                        
                    zdj.DATA_LIST_ZJ_RBS.append([env.now,NO_OF_ctzd])                   
                    env.process(convey(NO_OF_ctzd,zdj,env,TIME_ZD_MOVE))
                    # paper_change(INITIAL_LENGTH,zj_length,env,zdj)
        #回传的仿真结果--原纸剩余长度
        paper_change_trans(INITIAL_LENGTH,zj_length,env,zdj,SAMPLING_TIME,return_time_interval)
        #回传的仿真结果--折叠机入包数
        sim_result_trans(NO_OF_ctzd,env,zdj,return_time_interval,"186_D1544")
        #回传的仿真结果--折叠机出包数
        sim_result_trans_csb(zdj.zdj_cbs,env,zdj,return_time_interval,"190_D1710")


             
                                         
def convey(no_of_rbs,zdj,env,TIME_ZD_MOVE):    
    yield env.timeout(TIME_ZD_MOVE)                
    zdj.zdj_cbs=no_of_rbs                        
    zdj.zdj_cbs_list.append([env.now,zdj.zdj_cbs])             
# def paper_change(ini_length,zj_length,env,zdj):    
#     paper_length=[]
#     for i in range(len(ini_length)):
#         if ini_length[i]>10:
#             paper_length.append(ini_length[i]-zj_length*0.983)
#         else :
#             paper_length.append(ini_length[i])
#     zdj.paperLength_list.append([env.now,paper_length])
#回传的仿真结果--原纸剩余长度，需要重点考虑采样时间与返回时间间隔的关系
def paper_change_trans(ini_length,zj_length,env,zdj,SAMPLING_TIME,return_time_interval):
    # if env.now==SAMPLING_TIME:#待改进
    #     for i in range(len(ini_length)):
    #         zdj.paperLength_list.append(str(ini_length[i]))   
    if env.now-return_time_interval*zdj.num_record_syms>=0:
        zdj.num_record_syms=zdj.num_record_syms+1
        for i in range(len(ini_length)):
            zdj.paperLength_list[i] = zdj.paperLength_list[i]+","+str(ini_length[i]-zj_length*0.983)

def sim_result_trans(num,env,zdj,return_time_interval,type):
    
    if env.now-return_time_interval*zdj.num_record_rbs>=0: #待改进
        zdj.num_record_rbs=zdj.num_record_rbs+1
        if type=="186_D1544":
            zdj.zdj_rbs_trans = zdj.zdj_rbs_trans+","+str(num)
        elif type=="190_D1710":
            zdj.zdj_cbs_trans = zdj.zdj_cbs_trans+","+str(num)

def sim_result_trans_csb(num,env,zdj,return_time_interval,type):
    
    if env.now-return_time_interval*zdj.num_record_cbs>=0: #待改进
        zdj.num_record_cbs=zdj.num_record_cbs+1
        if type=="186_D1544":
            zdj.zdj_rbs_trans = zdj.zdj_rbs_trans+","+str(num)
        elif type=="190_D1710":
            zdj.zdj_cbs_trans = zdj.zdj_cbs_trans+","+str(num)

        
  





                        
                


            
            
            
            
        

