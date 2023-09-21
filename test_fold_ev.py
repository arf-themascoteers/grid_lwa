from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    c = FoldEvaluator(prefix="all", folds=10, algorithms=["ann"])
    c.process()