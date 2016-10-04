

(define (square-tree t)
 	(tree (square (entry t)))
		(if (leaf? t)
		 	nill
			(map square-tree (children t)))
