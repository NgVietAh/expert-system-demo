1. Cấu trúc phân cụm:
Có 3 cụm rõ rệt: Cụm 0 (xanh dương), Cụm 1 (cam), Cụm 2 (xanh lá).

Các cụm tách biệt tương đối rõ ràng, cho thấy dữ liệu có tính phân nhóm tốt sau khi chuẩn hóa + PCA.

2. Nhận xét về PCA:
@PCA đã giúp giảm chiều dữ liệu từ 7 đặc trưng → 2 thành phần chính (PC1 và PC2).

@PC1 đại diện cho mức độ tổng quát về ảnh hưởng COVID-19, vì nó kết hợp mạnh các yếu tố có hệ số lớn:

total_cases_per_million, total_vaccinations_per_hundred, median_age, gdp_per_capita.
| Đặc trưng                         |Trọng số|
| --------------------------------- | -------|
| total_cases_per_million           | 0.5444 |
| total_vaccinations_per_hundred    | 0.4841 |
| median_age                        | 0.5360 |
| gdp_per_capita                    | 0.2701 |
| hospital_beds_per_thousand        | 0.2418 |
 @PC1 phản ánh mức độ phát triển và ảnh hưởng dịch bệnh:

Nước có PC1 cao:
→ Dịch bùng phát nhiều, dân số già, tỷ lệ tiêm chủng cao, GDP cao.

Nước có PC1 thấp:
→ Dân số trẻ, ít ca nhiễm, tiêm chủng thấp, thu nhập thấp hơn.

@PC2 đại diện cho mức độ y tế và kiểm soát dịch, vì nó liên quan nhiều đến:

total_vaccinations_per_hundred (tích cực), total_deaths_per_million (tiêu cực), gdp_per_capita và hospital_beds_per_thousand.
| Đặc trưng                         |Trọng số|
| --------------------------------- | -------|
| total_vaccinations_per_hundred    | 0.6621 |
| gdp_per_capita                    | 0.3202 |
| total_deaths_per_million          |-0.4524 |
| hospital_beds_per_thousand        |-0.4001 |
@PC2 phản ánh khả năng kiểm soát dịch và hiệu quả y tế:

PC2 cao:
→ Tỷ lệ tiêm chủng cao, tử vong thấp, GDP tốt → kiểm soát dịch hiệu quả.

PC2 thấp:
→ Tử vong cao, hệ thống y tế kém, tiêm chủng ít → kiểm soát dịch kém.

3. Nhận xét biểu đồ phân cụm
Dựa vào hình ảnh bạn cung cấp và ý nghĩa PC1/PC2, ta có thể đưa ra nhận xét từng cụm như sau:

@Cụm 0 (màu xanh dương – nằm bên trái biểu đồ)
PC1 thấp → ít ca nhiễm, tiêm chủng thấp, dân số trẻ, GDP thấp.

PC2 gần 0 hoặc âm nhẹ → kiểm soát dịch không quá tốt, y tế còn yếu.

-->Nhóm các nước đang phát triển, dân số trẻ, ít tiêm chủng

@Cụm 1 (màu cam – nằm bên phải biểu đồ)
PC1 cao → nhiều ca nhiễm, tiêm chủng cao, dân số già, GDP cao.

PC2 cao → tử vong thấp, tiêm chủng mạnh, hệ thống y tế tốt.

-->Nhóm các nước phát triển, kiểm soát dịch tốt

@Cụm 2 (màu xanh lá – ở giữa)
PC1 trung bình → quốc gia ở mức phát triển trung bình.

PC2 phân tán từ cao đến thấp → kiểm soát dịch dao động mạnh.

-->Các nước đang phát triển cao hoặc chuyển tiếp