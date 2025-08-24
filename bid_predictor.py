 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/bid_predictor.py
index 0000000000000000000000000000000000000000..095a8a85be91bd955cd6e39c54a10ff264bd2f42 100644
--- a//dev/null
+++ b/bid_predictor.py
@@ -0,0 +1,67 @@
+"""Simple bidding prediction program for Nara Marketplace."""
+
+import random
+import statistics
+from typing import List, Tuple
+
+
+def generate_random_rates(min_rate: float, max_rate: float, count: int = 15) -> List[float]:
+    """Generate a list of random adjustment rates within the given range.
+
+    Args:
+        min_rate: Minimum adjustment rate.
+        max_rate: Maximum adjustment rate.
+        count: Number of random rates to generate.
+
+    Returns:
+        A list of random floating-point numbers.
+    """
+    return [random.uniform(min_rate, max_rate) for _ in range(count)]
+
+
+def predict_bid(
+    base_price: float,
+    participants: int,
+    min_rate: float,
+    max_rate: float,
+    lower_limit: float,
+    count: int = 15,
+) -> Tuple[float, float, List[float]]:
+    """Predict the winning bid price based on random adjustment rates.
+
+    The participants value is used as a random seed to keep the prediction
+    deterministic for a given number of participants.
+
+    Args:
+        base_price: Base estimated price.
+        participants: Number of participating companies (used for seeding).
+        min_rate: Minimum of the adjustment rate range.
+        max_rate: Maximum of the adjustment rate range.
+        lower_limit: Minimum allowed adjustment rate.
+        count: Number of random rates to generate.
+
+    Returns:
+        A tuple of (predicted_price, predicted_rate, rates_list).
+    """
+    random.seed(participants)
+    rates = generate_random_rates(min_rate, max_rate, count)
+    expected_rate = statistics.mean(rates)
+    predicted_rate = max(expected_rate, lower_limit)
+    predicted_price = base_price * predicted_rate
+    return predicted_price, predicted_rate, rates
+
+
+if __name__ == "__main__":
+    base_price = float(input("기초예가를 입력하세요: "))
+    participants = int(input("참가업체수를 입력하세요: "))
+    min_rate = float(input("사정률 범위의 최소값을 입력하세요 (예: 0.84): "))
+    max_rate = float(input("사정률 범위의 최대값을 입력하세요 (예: 1.0): "))
+    lower_limit = float(input("낙찰하한선을 입력하세요 (예: 0.87): "))
+
+    predicted_price, predicted_rate, rates = predict_bid(
+        base_price, participants, min_rate, max_rate, lower_limit
+    )
+
+    print("생성된 사정률:", ", ".join(f"{r:.5f}" for r in rates))
+    print(f"예상 사정률: {predicted_rate:.5f}")
+    print(f"예상 낙찰가격: {predicted_price:.0f}")
 
EOF
)
