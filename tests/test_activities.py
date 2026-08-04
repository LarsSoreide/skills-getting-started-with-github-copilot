def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == 9
    assert "Chess Club" in payload
    assert "Programming Class" in payload


def test_get_activities_contains_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    chess = response.json()["Chess Club"]
    assert "description" in chess
    assert "schedule" in chess
    assert "max_participants" in chess
    assert "participants" in chess
