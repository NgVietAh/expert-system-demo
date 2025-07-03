1. Nhận xét biểu đồ Elbow
@Trục hoành (x): Số cụm (k)
Giá trị từ 1 đến 10.

@Trục tung (y): Inertia
Là tổng bình phương khoảng cách nội cụm (within-cluster sum of squares – WCSS).

Giá trị càng nhỏ thì các điểm càng gần tâm cụm hơn.

2. Biểu đồ cho thấy:
Từ k = 1 → k = 3, Inertia giảm rất mạnh, chứng tỏ việc chia thêm cụm giúp cải thiện đáng kể độ chính xác.

Từ k = 3 → k = 4, độ dốc giảm rõ rệt, biểu đồ bắt đầu “gãy khúc”.

Từ k ≥ 4, Inertia tiếp tục giảm chậm, nghĩa là chia thêm cụm không còn mang lại nhiều cải thiện nữa.

3. Kết luận: Số cụm tối ưu là k = 3
Tại k = 3 là điểm “gãy” của biểu đồ → gọi là elbow point.

Đây là số cụm tối ưu, vì sau đó lợi ích của việc chia nhỏ thêm là không đáng kể.
4. Nhận xét:
Biểu đồ Elbow cho thấy rằng từ k = 1 đến k = 3, tổng khoảng cách nội cụm (Inertia) giảm mạnh, chứng tỏ việc tăng số cụm mang lại hiệu quả phân nhóm rõ rệt. 
Tuy nhiên, từ k = 4 trở đi, độ giảm của Inertia không còn đáng kể, biểu đồ bắt đầu tạo "elbow" tại k = 3. ==> Do đó, k = 3 được xác định là số cụm tối ưu cho bài toán phân cụm này.

