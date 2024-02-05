"""The SQLAlchemy Session object is the primary interface for all ORM operations. Here are some of the most commonly used methods:

add(instance): Adds an instance to the session for persistent operation. This object will be inserted into the database when the transaction is committed.

add_all([instances]): Adds a collection of instances to the session.

delete(instance): Marks an instance to be removed from the database at the next transaction commit.

commit(): Flushes any remaining changes to the database and commits the transaction. After the session's transaction is committed, the session's transaction is cleared.

rollback(): Rolls back the current transaction in progress.

query(class): Returns a new Query object which loads instances of a class.

flush(): Flushes all the object changes to the database (but does not commit the

Keyword arguments:
argument -- description
Return: return_description
"""
