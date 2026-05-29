import httpx

def test_fee_calculation():
    payload = {"distance_km": 5, "weight_kg": 50}
    response = httpx.post("http://localhost:8080/calculate-fee/", json=payload)
    assert response.status_code == 200
    assert "delivery_fee" in response.json()
