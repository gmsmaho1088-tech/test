"""Windows desktop unit price calculator tool."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


UNIT_PRICES = [60.0, 66.6, 80.0, 100.0, 120.0]


class UnitPriceCalculator(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=16)
        self.master.title("単価計算ツール")
        self.master.resizable(False, False)

        self.quantity_vars: list[tk.StringVar] = []
        self.result_vars: list[tk.StringVar] = []

        self._build_ui()

    def _build_ui(self) -> None:
        header = ttk.Label(self, text="単価計算ツール", font=("Yu Gothic UI", 14, "bold"))
        header.grid(row=0, column=0, columnspan=5, pady=(0, 10), sticky="w")

        ttk.Label(self, text="数量").grid(row=1, column=0, padx=4, pady=4)
        ttk.Label(self, text="単価").grid(row=1, column=1, padx=4, pady=4)
        ttk.Label(self, text="=").grid(row=1, column=2, padx=4, pady=4)
        ttk.Label(self, text="金額").grid(row=1, column=3, padx=4, pady=4)

        for i, unit_price in enumerate(UNIT_PRICES, start=2):
            quantity_var = tk.StringVar(value="0")
            result_var = tk.StringVar(value="0.00円")
            self.quantity_vars.append(quantity_var)
            self.result_vars.append(result_var)

            entry = ttk.Entry(self, width=10, textvariable=quantity_var)
            entry.grid(row=i, column=0, padx=4, pady=4)
            entry.bind("<KeyRelease>", lambda _event: self.recalculate())

            ttk.Label(self, text=f"× {unit_price:g}円").grid(row=i, column=1, padx=4, pady=4, sticky="w")
            ttk.Label(self, text="=").grid(row=i, column=2, padx=4, pady=4)
            ttk.Label(self, textvariable=result_var, width=12).grid(row=i, column=3, padx=4, pady=4, sticky="e")

        ttk.Separator(self, orient="horizontal").grid(row=len(UNIT_PRICES) + 2, column=0, columnspan=4, sticky="ew", pady=8)

        self.total_var = tk.StringVar(value="合計: 0.00円")
        ttk.Label(self, textvariable=self.total_var, font=("Yu Gothic UI", 11, "bold")).grid(
            row=len(UNIT_PRICES) + 3, column=0, columnspan=4, sticky="e"
        )

        note = ttk.Label(self, text="※ 数量を入力すると自動計算されます。")
        note.grid(row=len(UNIT_PRICES) + 4, column=0, columnspan=4, sticky="w", pady=(8, 0))

        self.grid()

    def recalculate(self) -> None:
        total = 0.0
        for quantity_var, unit_price, result_var in zip(self.quantity_vars, UNIT_PRICES, self.result_vars):
            quantity_text = quantity_var.get().strip()
            try:
                quantity = float(quantity_text) if quantity_text else 0.0
                amount = quantity * unit_price
                total += amount
                result_var.set(f"{amount:,.2f}円")
            except ValueError:
                result_var.set("入力エラー")
        self.total_var.set(f"合計: {total:,.2f}円")


def main() -> None:
    root = tk.Tk()
    UnitPriceCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
