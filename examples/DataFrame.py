import time

from ChallengerDeep.ChallengerDeep import *

if __name__=="__main__":
    
    file_path="file.csv"    

    pandas_start_time=time.time()
    processed_data=FilePandas.read_file(file_path)
    df=DataFramePandas(data=processed_data)
    pandas_time=time.time()-pandas_start_time
    df_filtered=df.filter_dataframe(columns=['commodity_name','state','district','market','min_price','max_price','modal_price','date'],conditions=['=','*','*','*','*','*','*','*'],values=['Ajwan','','','','','',''])
    print(df_filtered.tail_dataframe(n=5))
    out_path="pandas_file.csv"
    def reformat_ts(value):
        parts=value.split('-')
        if len(parts[-1])==4:
            parts=parts[::-1]
        return '-'.join(parts)
    df.df['date']=df.df['date'].apply(reformat_ts)
    FilePandas.write_file(file_path=out_path,data=df.df)
    print('Pandas Process',pandas_time)

    dask_start_time=time.time()
    processed_data=FileDask.read_file(file_path)
    df=DataFrameDask(data=processed_data)
    dask_time=time.time()-dask_start_time
    df_filtered=df.filter_dataframe(columns=['commodity_name','state','district','market','min_price','max_price','modal_price','date'],conditions=['=','*','*','*','*','*','*'],values=['Ajwan','','','','',''])
    print(df_filtered.tail_dataframe(n=5))
    out_path="dask_file.csv"
    def reformat_ts(value):
        parts=value.split('-')
        if len(parts[-1])==4:
            parts=parts[::-1]
        return '-'.join(parts)
    df.df['date']=df.df['date'].apply(reformat_ts,meta=('split_col','object'))
    FileDask.write_file(file_path=out_path,data=df.df)
    print('Dask Process',dask_time)

    custom_start_time=time.time()
    processed_data=CustomFileThread.read_file(file_path,num_threads=None,delimiter=',',datatypes=['str','str','str','str','float','float','float','str'])
    df=CustomDataFrameThread(data=processed_data,column_names=processed_data[0])
    custom_time=time.time()-custom_start_time
    df_filtered=df.filter_dataframe(columns=['commodity_name','state','district','market','min_price','max_price','modal_price','date'],conditions=['=','*','*','*','*','*','*'],values=['Ajwan','','','','',''])
    print(df_filtered.tail_dataframe(n=5))
    out_path="thread_file.csv"
    for i in range(len(df.df)):
        date=df.df[i][-1]
        parts=date.split('-')
        if len(parts[-1])==4:
            parts=parts[::-1]
        df.df[i][-1]='-'.join(parts)
    CustomFileThread.write_file(file_path=out_path,data=[df.header]+df.df)
    print('Custom Thread',custom_time)

    custom_start_time=time.time()
    processed_data=CustomFileProcess.read_file(file_path,num_processes=None,delimiter=',',datatypes=['str','str','str','str','float','float','float','str'])
    df=CustomDataFrameProcess(data=processed_data,column_names=processed_data[0])
    custom_time=time.time()-custom_start_time
    df_filtered=df.filter_dataframe(columns=['commodity_name','state','district','market','min_price','max_price','modal_price','date'],conditions=['=','*','*','*','*','*','*'],values=['Ajwan','','','','',''])
    print(df_filtered.tail_dataframe(n=5))
    out_path="process_file.csv"
    for i in range(len(df.df)):
        date=df.df[i][-1]
        parts=date.split('-')
        if len(parts[-1])==4:
            parts=parts[::-1]
        df.df[i][-1]='-'.join(parts)
    CustomFileProcess.write_file(file_path=out_path,data=[df.header]+df.df)
    print('Custom Process',custom_time)
