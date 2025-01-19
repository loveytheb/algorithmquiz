def solution(chicken):
    total_chicken = chicken
    coupons = chicken
    
    while coupons >= 10:
        service_chicken = coupons // 10
        total_chicken += service_chicken
        coupons = service_chicken + (coupons % 10)
    
    return total_chicken - chicken  # 처음 주문한 치킨 수는 제외하고 서비스 치킨만 반환