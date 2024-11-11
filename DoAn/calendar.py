from tkinter import Tk, Button, Label
from tkcalendar import Calendar


def create_calendar(master: Tk):
    """Create a calendar widget.

    Args:
        master (Tk): The Tkinter root or Toplevel window to which the calendar widget will be attached.

    Returns:
        Calendar: The created calendar widget.
    """
    # Add Calendar
    created_calendar = Calendar(master=master, selectmode='day', year=2020, month=5, day=22)
    return created_calendar


def set_label_text(label: Label, text: str):
    """Set text to a label widget.

    Args:
        label (Label): The label widget to update.
        text (str): The text to set to the label.
    """
    label.config(text=text)


def update_date(label: Label, calendar: Calendar):
    """Update label with the selected date from the calendar.

    Args:
        label (Label): The label widget to update.
        calendar (Calendar): The calendar widget from which to retrieve the selected date.
    """
    selected_date = calendar.get_date()
    set_label_text(label, "Selected Date is: " + selected_date)


if __name__ == "__main__":
    # Create Object
    root = Tk()

    # Set geometry
    root.geometry("400x400")

    cal = create_calendar(master=root)  # Create calendar widget
    cal.pack(pady=20)  # Pack calendar widget

    # Add Button and Label
    button = Button(
        master=root,
        text="Get Date",
        command=lambda: update_date(date, cal)  # Lambda function to pass arguments
    )
    button.pack(pady=20)  # Pack button widget

    date = Label(root, text="")  # Create label widget
    date.pack(pady=20)  # Pack label widget

    # Execute Tkinter
    root.mainloop()