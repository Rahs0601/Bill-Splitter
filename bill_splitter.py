import streamlit as st


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def split(highest_payer, lowest_payer):
    for (k, v) in highest_payer.items():
        temp = v
        for (a, b) in lowest_payer.items():
            temp2 = b
            while temp != 0 and b != 0:
                if temp - temp2 == 0:
                    st.write(f"{a} has to pay {temp2}rs to {k}")
                    temp = 0
                    temp2 = 0
                    break
                elif temp - temp2 < 0:
                    st.write(f"{a} has to pay {temp}rs to {k}")
                    temp2 = temp2 - temp
                    temp = 0
                    break
                else:
                    st.write(f"{a} has to pay {temp2}rs to {k}")
                    temp = temp - temp2
                    temp2 = 0
                    break
            highest_payer[k] = temp
            lowest_payer[a] = temp2


def equal():
    peps = {}
    num = st.sidebar.number_input("Enter the number of people in the group:")
    num = int(num)
    for i in range(num):
        name = st.sidebar.text_input(f"Enter the name of person {i+1}:")
        amount = st.sidebar.number_input(f"Enter the amount contributed by {name}:")
        peps[name.title()] = amount

    avg = sum(peps.values()) / num
    st.write(f"Average contribution: {avg}")

    highest_payer = {k: v - avg for (k, v) in peps.items() if v > avg}
    sort_dict_by_value(highest_payer)
    lowest_payer = {k: avg - v for (k, v) in peps.items() if v < avg}
    sort_dict_by_value(lowest_payer)

    st.write("People who should receive:", highest_payer)
    st.write("People who should pay:", lowest_payer)
    split(highest_payer, lowest_payer)


def unequal():
    peps = {}
    num = st.sidebar.number_input("Enter the number of people in the group:")
    num = int(num)
    for i in range(num):
        names = st.sidebar.text_input(f"Enter the name of person {i+1}:")
        peps[names.title()] = 0

    # money paid by each person
    for (k, v) in peps.items():
        b = {}
        for i in peps.keys():
            name = i
            amount = st.sidebar.number_input(f"Enter the amount paid by {k} for {i}:")
            b[name.title()] = amount
            peps[k] = b

    # his bank
    bank = {}
    for (k, v) in peps.items():
        sum = 0
        for b in v.values():
            sum += b
        bank[k.title()] = sum

    for (k, v) in bank.items():
        st.write(f"Total money debited from {k}'s account is {v}")

    # total expenditure by individual for himself
    q = []
    for (k, v) in peps.items():
        for i in v.values():
            q.append(i)

    ex = []
    for i in range(len(q) - 1):
        sum1 = 0
        while i <= len(q) - 1:
            sum1 += q[i]
            i += num
        ex.append(sum1)

    z = {}
    j = 0
    for (k, v) in peps.items():
        z[k.title()] = ex[j]
        j += 1
    st.write("Spent:", z)
    highest_payer = {}
    lowest_payer = {}
    for (k, v) in bank.items():
        for (a, b) in z.items():
            if k == a:
                if v > b:
                    highest_payer[k.title()] = v - b
                else:
                    lowest_payer[k.title()] = b - v
    st.write("People who should receive:", highest_payer)
    st.write("People who should pay:", lowest_payer)
    split(highest_payer, lowest_payer)


def main():
    st.title("Welcome to the Bill Splitter")
    # num = st.number_input("Enter the number of people:")
    ans = st.radio("Is the bill being split equally?", ("Yes", "No"))
    if ans == "Yes":
        try:
            equal()
        except:
            pass
    else:
        try:
            unequal()
        except:
            pass


if __name__ == "__main__":
    main()
