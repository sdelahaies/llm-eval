from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric


def test_relevancy():
    relevancy_metric = AnswerRelevancyMetric(threshold=0.5, model="gpt-4o")
    test_case_1 = LLMTestCase(
        input="Can I return these shoes after 30 days?",
        actual_output="Unfortunately, returns are only accepted within 30 days of purchase.",
        retrieval_context=[
            "All customers are eligible for a 30-day full refund at no extra cost.",
            "Returns are only accepted within 30 days of purchase.",
        ],
    )
    assert_test(test_case_1, [relevancy_metric])
