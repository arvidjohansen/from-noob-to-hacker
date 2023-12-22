
1. **SOLID Principles:**
   - **Single Responsibility Principle (SRP):** A class should have only one reason to change, meaning that it should have only one responsibility.
   - **Open/Closed Principle (OCP):** Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
   - **Liskov Substitution Principle (LSP):** Subtypes must be substitutable for their base types without altering the correctness of the program.
   - **Interface Segregation Principle (ISP):** A class should not be forced to implement interfaces it does not use.

2. **KISS (Keep It Simple, Stupid):** The principle states that simplicity should be a key goal and unnecessary complexity should be avoided.

3. **YAGNI (You Ain't Gonna Need It):** Don't add functionality until it is actually needed. This helps prevent over-engineering and keeps the focus on current requirements.

4. **Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules, but both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

5. **Law of Demeter (LoD or "Principle of Least Knowledge"):** A module should not know about the internal workings of the objects it manipulates, meaning that an object should only talk to its immediate neighbors.

6. **Composition Over Inheritance:** Favor composition (building complex objects by combining simpler ones) over inheritance (creating a new class by inheriting from an existing class).

7. **GRASP (General Responsibility Assignment Software Patterns):** These are a set of principles to guide the assignment of responsibility to classes and objects in object-oriented design.

8. **Fail Fast:** Identify and report errors as soon as they occur, rather than allowing them to propagate, making debugging easier.

9. **Separation of Concerns (SoC):** Divide a software system into distinct sections, each addressing a separate concern. This makes the system more modular and easier to maintain.

10. **Convention Over Configuration:** Reduce the number of decisions developers need to make by relying on conventions. This is often seen in frameworks where sensible defaults are used, and configuration is only needed when deviating from those defaults.

---

# NASA Principles for software design
NASA (National Aeronautics and Space Administration) has developed and adheres to specific software engineering principles to ensure the reliability, safety, and correctness of the software used in space missions. These principles are critical given the high-stakes nature of space exploration. Here are some key principles that NASA follows:

1. **Formal Methods:**
   - NASA often employs formal methods for software development, which involve the use of mathematical techniques to specify and verify the correctness of software systems.

2. **Requirement Analysis:**
   - Thorough requirements analysis is crucial. Clear, complete, and unambiguous requirements are essential for designing and building reliable software.

3. **Documentation:**
   - Extensive documentation is a key aspect of NASA's software development process. Detailed documentation helps in understanding, maintaining, and verifying the software throughout its lifecycle.

4. **Testing and Verification:**
   - Rigorous testing and verification processes are in place to identify and address defects in the software. This includes unit testing, integration testing, system testing, and formal verification methods.

5. **Safety-Critical Systems Standards:**
   - Adherence to safety-critical systems standards, such as DO-178C for avionics software, is common in NASA projects. These standards provide guidelines for the development and certification of software used in airborne systems.

6. **Independence and Redundancy:**
   - NASA often employs redundancy and independence in both hardware and software to enhance fault tolerance. Redundant systems can take over in case of a failure, ensuring the reliability of the overall system.

7. **Configuration Management:**
   - Strict configuration management practices are followed to control and track changes to the software throughout its development and operational lifecycle.

8. **Real-Time Systems Considerations:**
   - Many NASA missions involve real-time systems, where software must respond to events within specific time constraints. Real-time considerations are integral to the design and development of such systems.

9. **Human Factors Engineering:**
   - Consideration of human factors is essential in designing user interfaces and interactions, especially for manned space missions where astronauts interact with software systems.

10. **Security:**
    - Security is a critical concern, and NASA takes measures to ensure that software systems are protected from unauthorized access and potential cyber threats.

11. **Continuous Monitoring and Maintenance:**
    - Continuous monitoring and maintenance of software systems are performed throughout their operational life to address any issues that may arise and to ensure continued reliability.

It's important to note that the specific principles and practices may vary across different NASA projects and missions, and they are often tailored to the specific requirements and constraints of each mission. The overarching goal is to ensure the highest standards of reliability and safety in software systems used in space exploration.