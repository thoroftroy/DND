import tkinter as tk
from tkinter import ttk
import random

class Symbol:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

# Main application class
class SymbolManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Symbol Manager")
        self.root.geometry("800x600")

        # Set up custom style for background color
        style = ttk.Style()
        style.configure("Background.TFrame", background="black")

        # Section 1: Tabs for symbols
        self.symbol_tabs = ttk.Notebook(self.root)
        self.symbol_tabs.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="nsew")

        # Define lists for each tab
        tab_lists = {
            "Xerath": ["Carbon", "Oxygen", "Helium", "Neon","Phosphorus","Silicon","Sulfur","Titanium","Iron","Cobalt","Gallum","Arsenic","Silver","Tungston","Osmium","Platinum","Gold","Mercury","Uranium","Neptunium"],
            "Serenite": ["Freeze", "Shield", "Hail", "Vortex", "Still", "Mystic", "Calm", "Cascade", "Spectal", "", "", "", "", "", "", "", "", "", "", ],
            "Vindroth": ["I", "J", "K", "L"]
        }

        for symbol_type, tab_symbols in tab_lists.items():
            tab = ttk.Frame(self.symbol_tabs, style="Background.TFrame")
            self.symbol_tabs.add(tab, text=symbol_type)
            self.populate_symbol_tab(tab, tab_symbols)

        # Section 2: Toolbar
        self.toolbar = ttk.Frame(self.root, style="Background.TFrame")
        self.toolbar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.current_tool = tk.StringVar()
        tools = ["Inspect", "Erase", "Clear All"]
        for tool in tools:
            ttk.Radiobutton(self.toolbar, text=tool, variable=self.current_tool, value=tool, command=self.select_tool).pack(anchor="w")

        # Section 3: Symbol Information
        self.symbol_info = ttk.Frame(self.root, style="Background.TFrame")
        self.symbol_info.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.name_var = tk.StringVar()
        self.x_var = tk.StringVar()
        self.y_var = tk.StringVar()

        tk.Label(self.symbol_info, text="Name:", bg="black", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.symbol_info, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.symbol_info, text="X:", bg="black", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.symbol_info, textvariable=self.x_var).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.symbol_info, text="Y:", bg="black", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.symbol_info, textvariable=self.y_var).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        tk.Button(self.symbol_info, text="Confirm", command=self.confirm_edit).grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Section 4: Symbol List
        self.symbol_list = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="black", fg="white")
        self.symbol_list.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Section 5: Symbol Spawn Area
        self.spawn_area = tk.Canvas(self.root, bg="black", width=200, height=200)
        self.spawn_area.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        # Initialize data structures
        self.symbols = []

        # Set default tool
        self.current_tool.set("Inspect")

        # Binding events
        self.symbol_list.bind("<ButtonRelease-1>", self.select_symbol_from_list)
        self.spawn_area.bind("<Button-1>", self.spawn_symbol)
        self.spawn_area.bind("<B1-Motion>", self.move_symbol_wrapper)

    def populate_symbol_tab(self, tab, symbol_list):
        # Add symbols to the tab
        for i, symbol in enumerate(symbol_list):
            button = ttk.Button(tab, text=symbol, command=lambda s=symbol: self.spawn_symbol_from_tab(s, symbol_list))
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    def select_tool(self):
        # Handle tool selection
        tool = self.current_tool.get()
        if tool == "Clear All":
            self.clear_all_symbols()
            self.current_tool.set("Inspect")
        elif tool == "Erase":
            self.current_tool.set("Erase")

    def erase_symbol(self, symbol):
        # Erase the symbol from the canvas
        self.spawn_area.delete(symbol.name)

        # Remove the symbol from the list
        self.symbols.remove(symbol)

        # Update the symbol list and spawn area
        self.update_symbol_list()
        self.update_spawn_area()

    def spawn_symbol_from_tab(self, symbol, symbol_type):
        # Spawn symbol from the tabs
        x = random.randint(9, 250)  # Replace with semi-randomized location
        y = random.randint(19, 200)  # Replace with semi-randomized location
        self.spawn_symbol(symbol, x, y, symbol_type)

    def spawn_symbol(self, symbol, x, y, symbol_type=None):
        # Spawn symbol on the canvas
        new_symbol = Symbol(symbol, x, y)
        self.symbols.append(new_symbol)
        x_relative = self.spawn_area.winfo_reqwidth() // 2 + x  # Adjust for relative coordinates
        y_relative = self.spawn_area.winfo_reqheight() // 2 + y  # Adjust for relative coordinates
        symbol_item = self.spawn_area.create_text(x_relative, y_relative, text=symbol, fill="white", tags=(new_symbol,))
        self.update_symbol_list()
        self.update_spawn_area()

    def move_symbol(self, event, symbol):
        # Move the symbol on the canvas
        x, y = event.x, event.y
        x_relative = self.spawn_area.winfo_reqwidth() // 2 + x  # Adjust for relative coordinates
        y_relative = self.spawn_area.winfo_reqheight() // 2 + y  # Adjust for relative coordinates
        self.spawn_area.coords(symbol.name, x_relative, y_relative)
        symbol.x = x_relative - self.spawn_area.winfo_reqwidth() // 2  # Update relative X
        symbol.y = y_relative - self.spawn_area.winfo_reqheight() // 2  # Update relative Y
        self.update_symbol_info(symbol)
        self.update_spawn_area()

    def move_symbol_wrapper(self, event):
        tool = self.current_tool.get()
        if tool == "Inspect":
            selected_index = self.symbol_list.curselection()
            if selected_index:
                selected_symbol = self.symbols[selected_index[0]]
                self.move_symbol(event, selected_symbol)
        elif tool == "Erase":
            # Check if dragging or clicking to erase
            if event.type == "B1-Motion":
                self.erase_symbol_on_drag(event)
            elif event.type == "ButtonRelease":
                self.erase_symbol_on_click(event)

    def erase_symbol_on_drag(self, event):
        # Check if the cursor is over a symbol
        item = self.spawn_area.find_closest(event.x, event.y)
        if item:
            item_tags = self.spawn_area.gettags(item)
            if item_tags:
                erased_symbol = next((symbol for symbol in self.symbols if symbol == item_tags[0]), None)
                if erased_symbol:
                    self.erase_symbol(erased_symbol)

    def erase_symbol_on_click(self, event):
        # Check if the cursor is over a symbol
        item = self.spawn_area.find_closest(event.x, event.y)
        self.spawn_area.delete(item)
        if item:
            item_tags = self.spawn_area.gettags(item)
            if item_tags:
                erased_symbol = next((symbol for symbol in self.symbols if symbol == item_tags[0]), None)
                if erased_symbol:
                    self.erase_symbol(erased_symbol)

    def clear_all_symbols(self):
        # Clear all symbols on the canvas
        self.spawn_area.delete("all")
        self.symbols = []
        self.update_symbol_list()
        self.update_spawn_area()

    def update_symbol_list(self):
        # Update the symbol list
        self.symbol_list.delete(0, tk.END)
        for symbol in self.symbols:
            self.symbol_list.insert(tk.END, symbol.name)

    def select_symbol_from_list(self, event):
        # Select symbol from the list
        tool = self.current_tool.get()
        if tool == "Inspect":
            selected_index = self.symbol_list.nearest(event.y)
            if selected_index:
                selected_symbol = self.symbols[selected_index]
                self.update_symbol_info(selected_symbol)
                self.spawn_area.focus_set()

    def update_symbol_info(self, symbol):
        # Update symbol information in Section 3
        self.name_var.set(symbol.name)
        self.x_var.set(symbol.x)
        self.y_var.set(symbol.y)

    def confirm_edit(self):
        # Confirm the edit and update the selected symbol
        selected_index = self.symbol_list.curselection()
        if selected_index:
            selected_symbol = self.symbols[selected_index[0]]
            selected_symbol.name = self.name_var.get()
            selected_symbol.x = int(self.x_var.get())
            selected_symbol.y = int(self.y_var.get())
            self.update_symbol_list()
            self.update_spawn_area()

    def update_spawn_area(self):
        # Update the symbols on the spawn area
        self.spawn_area.delete("all")
        for symbol in self.symbols:
            x_relative = (self.spawn_area.winfo_reqwidth() // 28 + symbol.x) - 10  # Adjust for relative coordinates
            y_relative = (self.spawn_area.winfo_reqheight() // 28 + symbol.y) - 15  # Adjust for relative coordinates
            self.spawn_area.create_text(x_relative, y_relative, text=symbol.name, fill="white", tags=(symbol,))

if __name__ == "__main__":
    root = tk.Tk()
    app = SymbolManagerApp(root)
    root.mainloop()
