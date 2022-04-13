# Salton Index (Cosine Similarity)

Salton Index is one of the many proximity-based methods for link prediction. It falls under the local method of similarity measure.

Formula for the same is:
S_xy=  |Γ(x)∩ Γ(y)|/√(k_x×k_y )

Screenshot of the formula:
<p align = "center">
<img src = "https://user-images.githubusercontent.com/55135657/163159328-0268d802-3f9d-43f1-b3ce-cb30ae0dbfa3.png">
</p>
  
This formula was taken from the site: https://cran.r-project.org/web/packages/linkprediction/vignettes/proxfun.html

# UNDERSTANDING THE CODE

The included code file "saltonIndex.py" is an attempt to recreate Similarity Index Function available in NetworkX Library. The networkX library has all the other major similarity index function like Adamic-Adar Index (nx.adamic_adar_index (Graph)), Jaccard Coefficient (nx.jaccard_coefficient (Graph)), Preferential Attachment (nx.preferential_attachment (Graph)), Resource Allocation Index (nx.resource_allocation_index (Graph)) etc.

Just like these networkx functions, this saltonIndex.py code also has the prime function which takes the parameter Graph in the form salton_index (Graph).

THIS CODE GIVES THE FOLLOWING EXAMPLE OUTPUT:

![image](https://user-images.githubusercontent.com/55135657/163157901-b961c22f-c34d-407f-9254-d6a19a340fe8.png)

![image](https://user-images.githubusercontent.com/55135657/163158000-e25c699b-1bd3-4b0a-9138-848a561dd5e8.png)

The randomly generated graph for which the above obtained salton index values were calculated:
![image](https://user-images.githubusercontent.com/55135657/163157711-a2f1754d-5bea-47ba-8d60-57670eea5929.png)
The outputs may/will vary each time the code is executed as this random graph is an Erdos Reny Model, created using the NetworkX Library Function erdos_reny_graph (10, 0.4). Similarly, in place of random graph, karate club graph, football club, dolphin network etc. can be taken.
