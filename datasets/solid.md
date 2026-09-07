# SOLID Principles for Java Development

The SOLID principles provide a foundation for building maintainable, scalable, and testable Java applications. They encourage clean architecture, clear responsibilities, and flexible design.

---

## **S — Single Responsibility Principle (SRP)**
A class should have one responsibility and one reason to change.  
In Java, this means avoiding “God classes” and keeping logic cohesive.

**Example:**  
`InvoiceCalculator` handles calculations; `InvoicePrinter` handles output.

---

## **O — Open/Closed Principle (OCP)**
Classes should be open for extension but closed for modification.  
Java supports this through interfaces, abstract classes, and polymorphism.

**Example:**  
Add new `PaymentMethod` implementations without modifying existing code.

---

## **L — Liskov Substitution Principle (LSP)**
Subclasses must behave consistently with their base classes.  
Violations often occur when overriding methods break expected behavior.

**Example:**  
A `Square` should not extend `Rectangle` if width/height constraints differ.

---

## **I — Interface Segregation Principle (ISP)**
Prefer small, focused interfaces over large, general-purpose ones.  
Clients should not depend on methods they do not use.

**Example:**  
Split a large `Worker` interface into `Workable`, `Feedable`, `Restable`.

---

## **D — Dependency Inversion Principle (DIP)**
Depend on abstractions, not concrete implementations.  
High-level modules should not be tightly coupled to low-level details.

**Example:**  
Inject `MessageService` implementations (`EmailService`, `SmsService`) via constructors or frameworks like Spring.

---

# Summary
SOLID helps Java developers write cleaner, more modular code.  
By applying these principles, systems become easier to maintain, extend, and test—especially in large-scale or long-lived applications.
