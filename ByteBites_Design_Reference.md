# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
- Use only the four classes in `bytebites_spec.md`: `Customer`, `FoodItem`, `Menu`, `Order`.
  Do not add helper, manager, or base classes (no `User`, `Cart`, `MenuManager`, `Payment`).
- Relate classes by composition, not inheritance. `Menu` and `Order` each hold a list of
  `FoodItem` objects. `Customer` holds a list of past `Order` objects. Nothing subclasses
  anything.
- Categories like "Drinks" or "Desserts" are a string on `FoodItem`, not separate classes.
- Only add attributes and methods the spec asks for. If you think something else is needed,
  say so and explain why instead of adding it.
- Put behavior where the data lives: filtering and sorting on `Menu`, the total on `Order`,
  adding past orders on `Customer`.
- Stick to the Python standard library. No dataclasses, ORMs, or third-party packages beyond
  `pytest` for tests.
- Filter and sort methods return a new list and leave the original list unchanged.
- When I ask for a diagram, give me a diagram, not code. When I ask for a scaffold, give me the
  constructor and attributes only, no method logic yet.
- Keep code short and readable. Explain any suggestion in one or two sentences.
