The purpose of this project is to use real-world data to map out relationships between benign (noncancerous) and malignant (cancerous) cells to identify any patterns.

*To view all the graphs, go to the file titled 'Breast Cancer Cell Data Graphs.ipynb'.*

----
**Observations:**

- There are more malignant cells than there are benign cells in the observed tissue. This is explained by the fact that breast cancer cells spread rapidly, leading to the number
of cancerous cells outnumbering the number of noncancerous cells.
- Benign cells, on average, have larger radii. The distribution is also more spread out, compared to malignant cells, which have smaller radii, within a smaller range as well.
- On average, the area of a benign cell is higher than that of a malignant cell. This observation is not surprising, as benign cells also have larger radii. Additionally, there is more fluctuation when it comes to the area of the benign cells, compared to the malignant cells.
- The mean perimeter of benign cells is, unsurprisingly, larger than that of the malignant cells. The mean perimeter data for benign cells also fluctuates more throughout a larger range.
- There is a proportional relationship between the texture of benign and malignant cells. Although there is a slight variation, the data for both cells fits under a similar range, and both graphs display a similar curve.
- Lastly, there is also a proportional relationship between the smoothness of benign and malignant cells. The data for both cells fits under a similar, uniform range. Furthermore, there is a slight variation, as on average, benign cells are slightly more smooth.

*\* 'target = 0.0' Indicates Benign Cells, 'target = 1.0' Indicates Malignant Cells*

![image](https://user-images.githubusercontent.com/86753980/126085278-d521f7ad-3f6a-4798-b067-801059192d4e.png)

----
**Final Comments**

The main takeaways from this project are that first, there are more malignant cells than benign cells in a sample of cancerous tissue. This is backed up by concrete scientific evidence, as breast cancer is widely known for being a type of cancer that spreads quickly. As a result, cancerous tissue would contain a higher volume of malignant cells, in comparison  to benign cells.

The next main takeaway is that benign cells are significantly larger than malignant cells. However, there is also more deviation when it comes to the size of the benign cells. The range of sizes for benign cells is twice that of malignant cells. The graph displaying the relationship between benign and malignant cells when looking at cell radius has a very similar shape to the Maxwell-Boltzmann Distribution.

----

***Cell Type vs. Mean Radius (Blue Indicates Benign, Red Indicates Malignant)***

![image](https://user-images.githubusercontent.com/86753980/126085150-d8376a29-be9c-4176-9963-0df8d92612d8.png)


***Maxwell-Boltzmann Distribution***

![image](https://user-images.githubusercontent.com/86753980/126085250-9dd83846-0cdd-49d0-a442-cfc4f25deef2.png)
