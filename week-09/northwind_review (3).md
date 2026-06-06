{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1d4889ca-ae41-4013-9a5b-4763e29f73a3",
   "metadata": {},
   "source": [
    "## Table: Categories\n",
    "**Primary Key:** CategoryID  \n",
    "**Parent Tables (Foreign Keys referenced by):** Products (CategoryID)\n",
    "\n",
    "| Column | What does a value in this column represent? What values might you see here? | Is this column a part of the primary key to this table? | Is this column a part of a foreign key that points to a record in another table? | Would this column be valuable to bring into our Power BI Model? Yes, or no? Why? | Do you believe this column is appropriately named for Data Analysis purposes? |If not, what might be a more appropriate name?| What might be the data type and format for this column in a Power BI Model? | Can you think of any calculations where this column data might be used? |\n",
    "|---|---|---|---|---|---|---|---|---|\n",
    "| CategoryID | A unique identifier assigned to each product category.Values are small integers (1–8) since there are only 8 categories in this database.| Yes | No | Yes –  It is needed to create the relationship between Categories and Products in the data model. | Yes | N/A - The name is appropriate. | Whole Number. No special format needed, it acts as a key not a value. | Primarily used for joining tables (relationship key), not direct calculations. Could be used in COUNTROWS or CALCULATE filters to count products per category. |\n",
    "| CategoryName | The name of the product category (e.g., Beverages, Seafood etc) | No | No | Yes – This is a key label used in charts, slicers, and filters to allow users to slice sales or product data by category. | Yes | N/A | Text |  Used as an axis or legend in visuals (e.g., Sales by Category bar chart). Can be used in CALCULATE with FILTER to isolate a specific category's metrics. |\n",
    "| Description | A short text description of the product category(e.g., \"Soft drinks, coffees, teas, beers, and ales\" for Beverages). | No | No | Probably not. Descriptions are rarely used in analysis or calculations; they may be useful in a tooltip visual. | It's acceptable, though generic. A name like \"CategoryDescription\" would be clearer.| CategoryDescription. | Text | Not typically used in calculations. Could appear as a tooltip or detail field in a report. |\n",
    "| Picture | A binary field storing an image associated with the category. Values are raw binary image data.| No | No | No. Binary image data is not usable in Power BI, and it adds no analytical value. | The name is clear, but the column itself is not relevant for data analysis. | N/A | It would likely be excluded. If kept, Power BI would import it as Binary, which is not directly usable.| None — this column should be excluded from the Power BI model. |\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b2f5ed3-1e18-4c53-89ec-80582588b4f4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6eb14b4-2d22-4882-a2f1-52f9133aac9c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
