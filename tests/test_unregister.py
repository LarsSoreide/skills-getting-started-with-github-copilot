def test_unregister_success_removes_participant(client):
    participant = "daniel@mergington.edu"

    response = client.delete(f"/activities/Chess Club/participants/{participant}")

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {participant} from Chess Club"
    }

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert participant not in participants


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown Club/participants/student@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_404(client):
    response = client.delete(
        "/activities/Chess Club/participants/not-enrolled@mergington.edu"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
