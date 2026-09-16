import streamlit as st
import pandas as pd

# Student Information
st.write("Name: THARANI A/P SEKAR")
st.write("Registration Number: 25DIT24F1139")
st.write("Class: DIT4B")
st.write("Course/Subject: DFK50083 - PYTHON PROGRAMMING")
st.write("Practical Work 3")

st.title("Student Printing Charges")

# Task 1: GUI and Input Components

# Lists to store student information
student_names = []
printing_types = []
number_of_pages = []
binding_options = []

# Number of students
num_students = st.number_input(
    "Number of Students",
    min_value=1,
    step=1
)

# Input for each student
for i in range(num_students):

    st.subheader("Student " + str(i + 1))

    name = st.text_input(
        "Student Name",
        key="name" + str(i)
    )

    printing_type = st.selectbox(
        "Printing Type",
        ["Black & White", "Colour", "Photo Printing"],
        key="printing" + str(i)
    )

    pages = st.text_input(
        "Number of Pages",
        key="pages" + str(i)
    )

    binding = st.selectbox(
        "Binding Option",
        ["Binding Required", "No Binding"],
        key="binding" + str(i)
    )

    # Store information in lists
    student_names.append(name)
    printing_types.append(printing_type)
    number_of_pages.append(pages)
    binding_options.append(binding)


# Required buttons
calculate_btn = st.button("Calculate")
summary_btn = st.button("View Summary")
display_btn = st.button("Display Record")
delete_btn = st.button("Delete Record")


# Function to determine price per page
def get_price(printing_type):

    if printing_type == "Black & White":
        return 0.20

    elif printing_type == "Colour":
        return 0.80

    else:
        return 1.20


# Task 2, Task 3 and Task 4: Calculate

if calculate_btn:

    for i in range(num_students):

        st.subheader("Calculation for " + student_names[i])

        try:
            # Convert number of pages to integer
            pages = int(number_of_pages[i])

            # Get price per page
            price_per_page = get_price(printing_types[i])

            # Calculate printing charge
            printing_charge = price_per_page * pages

            # Calculate binding charge
            if binding_options[i] == "Binding Required":
                binding_charge = 3.00
            else:
                binding_charge = 0.00

            # Calculate final total
            final_total = printing_charge + binding_charge

            # Calculate average cost per page
            average_cost = final_total / pages

            # Display calculation
            st.write(
                "Printing Charge: RM {:.2f}".format(printing_charge)
            )

            st.write(
                "Binding Charge: RM {:.2f}".format(binding_charge)
            )

            st.write(
                "Average Cost per Page: RM {:.2f}".format(average_cost)
            )

            st.success(
                "Final Total: RM {:.2f}".format(final_total)
            )

        except ValueError:
            st.error("Number of Pages must be an integer.")

        except ZeroDivisionError:
            st.warning("Number of Pages cannot be zero.")


# Task 3: View Summary

if summary_btn:

    st.subheader("PRINTING SUMMARY")

    for i in range(num_students):

        try:
            pages = int(number_of_pages[i])

            price_per_page = get_price(printing_types[i])

            printing_charge = price_per_page * pages

            if binding_options[i] == "Binding Required":
                binding_charge = 3.00
            else:
                binding_charge = 0.00

            final_total = printing_charge + binding_charge

            st.write("Student Name:", student_names[i])
            st.write("Printing Type:", printing_types[i])
            st.write("Number of Pages:", pages)
            st.write("Binding Option:", binding_options[i])

            st.write(
                "Final Total: RM {:.2f}".format(final_total)
            )

            st.divider()

        except ValueError:
            st.error(
                "Invalid Number of Pages for "
                + student_names[i]
            )


# Task 5: Display Record

if display_btn:

    st.subheader("STUDENT PRINTING RECORDS")

    for i in range(num_students):

        try:
            pages = int(number_of_pages[i])

            price_per_page = get_price(printing_types[i])

            printing_charge = price_per_page * pages

            if binding_options[i] == "Binding Required":
                binding_charge = 3.00
            else:
                binding_charge = 0.00

            final_total = printing_charge + binding_charge

            st.write("Student Name:", student_names[i])
            st.write("Printing Type:", printing_types[i])
            st.write("Number of Pages:", pages)
            st.write("Binding Option:", binding_options[i])

            st.write(
                "Price per Page: RM {:.2f}".format(price_per_page)
            )

            st.write(
                "Printing Charge: RM {:.2f}".format(printing_charge)
            )

            st.write(
                "Binding Charge: RM {:.2f}".format(binding_charge)
            )

            st.write(
                "Final Total: RM {:.2f}".format(final_total)
            )

            st.divider()

        except ValueError:
            st.error(
                "Invalid Number of Pages for "
                + student_names[i]
            )


# Task 5: Delete Record

if delete_btn:

    student_names = []
    printing_types = []
    number_of_pages = []
    binding_options = []

    st.success("Record deleted successfully!")