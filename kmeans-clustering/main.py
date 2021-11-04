import pandas as pd
import pprint
import matplotlib.pyplot as plt
from tqdm import tqdm

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score

pp = pprint.PrettyPrinter()


def kmeans_simple(data, cluster_range):
    inertias = []
    for num_cluster in tqdm(cluster_range, total=len(cluster_range)):
        model = KMeans(n_clusters=num_cluster)
        model.fit(data)
        inertias.append(model.inertia_)
   
    return inertias


def kmeans(data, distance_metric, k_max):
    sil = []
    for k in range(2, k_max+1):
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0).fit(data)
        labels = kmeans.labels_
        sil_coeff = silhouette_score(data, labels, metric=distance_metric )
        sil.append(sil_coeff)    
    
    return sil


def preprocess(dataframe):
    dataframe.rename(columns={"Unnamed: 0": "Name"}, inplace=True)
    dataframe.fillna(0, inplace=True)
    mms = MinMaxScaler()
    normalized_data = mms.fit_transform(dataframe[dataframe.columns[1:]])
    df_original = pd.DataFrame(normalized_data, columns=dataframe.columns[1:])
    return df_original


if __name__ == '__main__':
    df = pd.read_csv('data/sample.csv')
    df_original = preprocess(dataframe=df)

    # How many principal components must be used?
    pca = PCA(n_components=0.95)
    df_reduced = pca.fit_transform(df_original)
    assert(len(df_reduced[0]) < len(df_original.loc[0, :]))
    features = range(pca.n_components_)
    plt.bar(features, pca.explained_variance_ratio_, color='black')
    plt.xlabel('Principal Components')
    plt.ylabel('Variance %')
    plt.xticks(features)

    # How many clusters can we recognize? 1- Inertia 2- Silhouette 
    # 1
    cluster_range = range(1, 20)
    inertias_original = kmeans_simple(df_original, cluster_range)
    inertias_reduced = kmeans_simple(df_reduced, cluster_range)
    plt.figure()
    plt.plot(cluster_range, inertias_original, '-o', color='black', label='Original')
    plt.plot(cluster_range, inertias_reduced, '-o', color='red', label='Reduced')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.xticks(cluster_range)
    plt.legend()
    # 2
    k_max = 20
    sil_original = kmeans(df_original, 'euclidean', k_max)
    sil_reduced = kmeans(df_reduced, 'euclidean', k_max)
    plt.figure()
    plt.plot(range(2, k_max+1), sil_original, '-o', color='black', label='Original')
    plt.plot(range(2, k_max+1), sil_reduced, '-o', color='red', label='Reduced')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.xticks(range(2, k_max+1))
    plt.legend()

    # Visualization - num_cluster=3
    pca = PCA(n_components=2)
    df_reduced = pca.fit_transform(df_original)
    pca_components = pd.DataFrame(df_reduced)
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df_reduced)
    y_kmeans = kmeans.predict(df_reduced)
    centers = kmeans.cluster_centers_

    plt.figure()
    plt.scatter(pca_components[0], pca_components[1], c=y_kmeans, s=50, cmap='Set3')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200)


    # Print RESULTS
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df_original)
    y_kmeans = kmeans.predict(df_original)
    centers = kmeans.cluster_centers_

    res = list(zip(df['Name'], y_kmeans))
    clusters = {}
    for item in res:
        if item[1] in clusters:
            clusters[item[1]].append(item[0])
        else:
            clusters[item[1]] = []

    pp.pprint(clusters)
    plt.show()
