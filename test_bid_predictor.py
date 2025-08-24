 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/test_bid_predictor.py
index 0000000000000000000000000000000000000000..2992960f18972927beb7cf97043ac2bb08720358 100644
--- a//dev/null
+++ b/test_bid_predictor.py
@@ -0,0 +1,14 @@
+from bid_predictor import predict_bid
+
+
+def test_predict_bid_basic():
+    price, rate, rates = predict_bid(100000, 10, 0.8, 1.0, 0.85)
+    assert round(rate, 5) == 0.90917
+    assert round(price) == 90917
+    assert len(rates) == 15
+
+
+def test_predict_bid_with_lower_limit():
+    price, rate, _ = predict_bid(100000, 20, 0.7, 0.75, 0.85)
+    assert rate == 0.85
+    assert price == 85000
 
EOF
)
