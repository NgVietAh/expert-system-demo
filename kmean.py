import pandas as pd

# Bước 1: Đọc dữ liệu từ file (giả định tên file là 'owid-covid-data.csv')
file_path = r"C:/Vanh/Thuctap/expert-system-demo/owid-covid-data.csv"  
df = pd.read_csv(file_path, sep=';')

# In ra số lượng nước khác nhau ban đầu
print('Số nước khác nhau ban đầu:', df['location'].nunique())

# Bước 1: Data Cleaning & Preprocessing
# Chuyển đổi cột 'date' sang kiểu datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Lọc dữ liệu từ 2020-01-01 đến 2023-06-30
df = df[(df['date'] >= '2020-01-01') & (df['date'] <= '2023-06-30')]

# Loại bỏ các hàng không có thông tin quốc gia
df = df[df['location'].notna() & (df['location'] != 'World')]

# Chọn các cột cần dùng cho đề tài
columns_needed = [
    'iso_code', 'continent', 'location', 'date',
    'total_cases_per_million',
    'total_deaths_per_million',
    'total_vaccinations_per_hundred',
    'gdp_per_capita',
    'population_density',
    'hospital_beds_per_thousand',
    'median_age'
]

df = df[columns_needed]

# Loại bỏ hoàn toàn các dòng có NaN ở các thuộc tính cần thiết
df = df.dropna()

# Bước 2: Data Integration
# Tích hợp dữ liệu cấp quốc gia bằng cách lấy giá trị trung bình theo từng quốc gia
country_grouped = df.groupby('location').agg({
    'total_cases_per_million': 'mean',
    'total_deaths_per_million': 'mean',
    'total_vaccinations_per_hundred': 'mean',
    'gdp_per_capita': 'mean',
    'population_density': 'mean',
    'hospital_beds_per_thousand': 'mean',
    'median_age': 'mean'
}).reset_index()

# Chỉ giữ lại các nước có đủ thuộc tính (không có giá trị nào bằng 0)
country_grouped = country_grouped[(country_grouped.iloc[:, 1:] != 0).all(axis=1)]

# In ra số lượng nước đáp ứng đủ điều kiện (sau khi groupby và fillna)
print('Số nước đáp ứng đủ điều kiện:', country_grouped['location'].nunique())

# Bước 3: Data Transformation
# Chuẩn hóa dữ liệu bằng Min-Max Scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(country_grouped.iloc[:, 1:])  # Bỏ cột 'location'

# Tạo DataFrame đã chuẩn hóa
normalized_df = pd.DataFrame(normalized_data, columns=country_grouped.columns[1:])
normalized_df.insert(0, 'location', country_grouped['location'])

normalized_df.head()
print(normalized_df)

# Bước 4: K-means clustering và vẽ biểu đồ Elbow
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Chỉ lấy dữ liệu số để phân cụm (bỏ cột 'location')
X = normalized_df.iloc[:, 1:]

# Tìm giá trị k tối ưu bằng phương pháp Elbow
inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.xlabel('Số cụm (k)')
plt.ylabel('Inertia (Tổng bình phương khoảng cách nội cụm)')
plt.title('Biểu đồ Elbow để xác định số cụm tối ưu')
plt.grid(True)
plt.show()

# Sau khi xem biểu đồ Elbow, giả sử chọn k=3 (bạn có thể thay đổi giá trị này)
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
normalized_df['cluster'] = kmeans.fit_predict(X)

#Biểu đồ phân cụm
from sklearn.decomposition import PCA

# Giảm số chiều về 2D để trực quan hóa
pca = PCA(n_components=2)
components = pca.fit_transform(X)

# Tạo DataFrame cho biểu đồ
pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
pca_df['cluster'] = normalized_df['cluster']
pca_df['location'] = normalized_df['location']

# Vẽ scatter plot
plt.figure(figsize=(10, 6))
for cluster_id in sorted(pca_df['cluster'].unique()):
    clustered = pca_df[pca_df['cluster'] == cluster_id]
    plt.scatter(clustered['PC1'], clustered['PC2'], label=f'Cụm {cluster_id}', s=60)

plt.title('Biểu đồ phân cụm các quốc gia (sau PCA)')
plt.xlabel('PC1') #Thành phần chính 1
plt.ylabel('PC2') #Thành phần chính 2
plt.legend()
plt.grid(True)
plt.show()

# print("Trọng số của các đặc trưng trong PC1 và PC2:")
# for i, component in enumerate(pca.components_):
#     print(f"PC{i+1}:")
#     for feature, weight in zip(X.columns, component):
#         print(f"  {feature}: {weight:.4f}")

# In kết quả phân cụm
print(normalized_df[['location', 'cluster']])
# Nếu muốn lưu kết quả ra file:
normalized_df.to_csv('clustered_countries.csv', index=False, sep=';')