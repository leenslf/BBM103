# Leen Said 2220356194
import sys
fulllist_of_comp_data=[]
num=0
try:
    operands= sys.argv[1]
    comparison= sys.argv[2]
    def read_operands():
        f = open(operands, "r")
        read = f.readlines()
        return read
    def read_comparison():
        f = open(comparison, "r")
        read = f.readlines()
        return read

    for linecom in read_comparison():
        list_of_comp_data=linecom.split(" ")
        fulllist_of_comp_data.append(list_of_comp_data)
    for i in fulllist_of_comp_data:
        for k in i:
            if k[-1]=="\n":
                ii=i.index(k)
                oo=fulllist_of_comp_data.index(i)
                fulllist_of_comp_data[oo][ii]=k.replace("\n","")

    for line in read_operands():
        try:

            list_of_operands=line.split(" ")
            def calculator(list_operands):
                if type(list_operands[0])==str:
                    try:
                        div=int(list_operands[0])
                    except:
                        div=int(float(list_operands[0])-0.5)+1

                if type(list_operands[1])==str:
                    try:
                        nondiv=int(list_operands[1])
                    except:
                        nondiv=int(float(list_operands[1])-0.5)+1
                
                if type(list_operands[2])==str:
                    try:
                        lower_range=int(list_operands[2])
                    except:
                        lower_range=int(float(list_operands[2])-0.5)+1

                if type(list_operands[3])==str:
                    try:
                        upper_range=int(list_operands[3])
                    except:
                        upper_range=int(float(list_operands[3])-0.5)+1

                list_of_dev=[]
                for number in range(lower_range,upper_range+1):
                    if number%div==0 and number%nondiv!=0:
                        list_of_dev.append(str(number))
                return list_of_dev

            values=calculator(list_of_operands)
            
            print("------------")
            print("My results:",*values)
            print("Results to compare:",*fulllist_of_comp_data[num],end="")   
             
            if str(values)==(str(fulllist_of_comp_data[num])):
                print("\nGoool!!!") 
            else:
                raise AssertionError
            num+=1
                
        except AssertionError:
            num += 1
            print("\nAssertion Error: results don’t match.")
        except IndexError:
            num += 1
            print("------------")
            print("IndexError: number of operands less than expected.")
            print("Given input: ",*list_of_operands,end="")
        except ZeroDivisionError:
            num += 1
            print("------------")
            print("ZeroDivisionError: You can’t divide by 0.")
            print("Given input: ",*list_of_operands,end="")
        except ValueError:
            num += 1
            print("------------")
            print("ValueError: only numeric input is accepted.")
            print("Given input: ",*list_of_operands,end="")
        except Exception as k:
            print("------------")
            print("Unexpected error :",k)


except IOError as e:
    ss=str(e)
    sss=ss.split(" ")
    print("IOError:cannot open",sss[7])

except IndexError:  # we need two index error exceptions
    print("IndexError: number of input files less than expected.")

finally:
    print("˜ Game Over ˜")

