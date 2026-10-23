from __future__ import annotations

from pagescan.detector import to_bbox


def test_to_bbox_basic():
    points = [[10, 20], [30, 20], [30, 50], [10, 50]]
    assert to_bbox(points) == (10, 20, 30, 50)


def test_to_bbox_unsorted_points():
    points = [[15, 100], [80, 20], [10, 15], [45, 60]]
    assert to_bbox(points) == (10, 15, 80, 100)


def test_normalized_detection_has_json_safe_types():
    raw = ([[[0.0, 0.0], [10.0, 0.0], [10.0, 5.0], [0.0, 5.0]], "hello", 0.91],)
    item = None
    # Simulate the expected raw detection shape from EasyOCR.
    from pagescan.detector import normalize_detection

    item = normalize_detection("page1.png", raw[0], min_confidence=0.5)
    assert item is not None
    assert item["page"] == "page1.png"
    assert item["box"] == [0, 0, 10, 5]
    assert item["text"] == "hello"
    assert isinstance(item["confidence"], float)
