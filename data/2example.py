import pandas as pd

header = ["Filename", "term", "coursename", "description", "attempted","earned credits", "points", "grade"]
file1_data = []

def mapped_data(in_row={}):
    print('function called') 
    file1_data.append(in_row)
def process_example2():
    with open("Example_2.txt") as file1:
        counter, data_ind,term =1,1, ''
        while counter and data_ind<10:
            #print(counter, data_ind)
            temp,temp_dict = file1.readline().strip(), {}
            #print(temp, len(temp),'this is debug')
            try:
                if len(temp)==0:
                    data_ind+=1
                    #print(data_ind,'data_ind incremented')
                #if len(temp)==0:
                #    data_ind+=1
                if len(temp)>20:
                    #print('data_ind is reset')
                    data_ind=1
                if "-----------" in temp:
                    term = " ".join(temp.split(" ")[:2])
                if term and len(temp)>2 and isinstance(float(temp.split(" ")[-1]),float) and "-" in [i for i in temp.split(" ")][0] and temp.split(" ")[-4] in ("A","B","W"): 
                    temp_list=temp.split(" ")
                    coursename = temp_list[0]
                    attempted = str(temp_list[-3])
                    earned_credits = str(temp_list[-2])
                    points = str(temp_list[-1])
                    grade = temp_list[-4]
                    description = " ".join(temp_list[1:-4])
                    temp_dict.update({"Filename":file1.name,"term":term,"coursename":coursename, "description":description,"attempted":attempted,"earned credits":earned_credits, "points":points,"grade":grade})
                    mapped_data(temp_dict)
    
                counter+=1
            except Exception as e:
                continue
    print(file1_data)
    df1=pd.DataFrame(file1_data)
    df1.to_excel('output_example2.xlsx',index=False)
process_example2()

