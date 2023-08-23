import tkinter as tk


def display_contract(decrypted_contract):
    # Create main window
    root = tk.Tk()
    root.option_add('*Font', 'Helvetica 20 bold')
    root.title('Decrypted Contract')

    # Create a label to indicate the successful verification message
    verification_label = tk.Label(root, text="Signatures have been verified successfully!", wraplength=800, fg="green")
    verification_label.pack()

    # Creating a label for the heading "Decrypted Contract:"
    contract_heading = tk.Label(root, text="Decrypted Contract:", font='Helvetica 18')
    contract_heading.pack()

    # Create a text widget to display the contract
    text_widget = tk.Text(root, wrap=tk.WORD, font='Helvetica 14')
    text_widget.pack(expand=tk.YES, fill=tk.BOTH)

    # Adding the decrypted contract to the text widget
    text_widget.insert(tk.END, decrypted_contract)

    # Run main event loop
    root.mainloop()
