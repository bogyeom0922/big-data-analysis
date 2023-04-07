data <- read.csv(file="C:/Users/User/Documents/한국철도공사_수도권 전철 혼잡도_20181231.csv", header=T, fileEncoding = "euc-kr")
data
congestion <- data %>% select(c(최대.혼잡구간, 최고))
congestion

#각 구간별 최고 혼잡도 크기지만 모두 크기가 매우 다른 것을 알 수 있음
hist(congestion$최고, main="최고 혼잡도 크기 분포")

# 혼잡 구간에 따라 점으로 최고 혼잡도를 표시하여 구간별 차이를 나타냄
congestion %>% ggplot(aes(x=최고, y=최대.혼잡구간))+geom_point(alpha=0.2)


#출, 퇴근 가장 혼잡한 시간인 8시, 18시의 지하철 '하선'만 조사
s_data <- read.csv(file="C:/Users/User/Documents/서울교통공사_지하철혼잡도정보_20211231.csv", header=T, fileEncoding = "euc-kr")
s_data <- subset(s_data, 구분=='하선', select = -c(구분))
s_data

#출근, 퇴근 혼잡도 크기 비교
plot(s_data$퇴근, s_data$출근)

matplot(s_data[, 3:4], type="l", col = c("red", "blue"))
legend("topright", names(s_data)[3:4], lty=c(1,2), col = c("red", "blue"))

ggplot(s_data, aes(x=출근, y=퇴근))+geom_point()


# 출근길 역별 혼잡도 비교
ggplot(s_data, aes(출근))+geom_histogram()
barplot(s_data$출근, names.arg=s_data$역명)
ggplot(s_data, aes(역명, 출근))+geom_boxplot()

# 호선 별 비교
ggplot(s_data, aes(x=역명, y=출근, col=호선))+geom_point(alpha=0.5)+geom_smooth()
ggplot(s_data, aes(x=역명, y=출근))+geom_point(alpha=0.5)+facet_wrap(~호선)
