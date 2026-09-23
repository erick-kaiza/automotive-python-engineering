The project is a class based python tool that models a naturally aspirated engine and a turbocharged engine as a base class and subclass,comparing their performance on a simulated dyno test.

A turbocharged engine shares almost everything with a naturally aspirated one -displacement,cylinder count,torque,redline-but adds one extra factor:boost pressure,which increases the effective air (and therefore) the engine can produce.Rather than duplicating all the shared engine logic in two separate classes,this project uses inheritance

ENGINEERING CONTEXT

Comparing naturally aspirated and turbocharged variants of the same base engine is a standard exercise in powertrain performance analysis-it isolates exactly how much of a performance gain comes from forced induction versus other engine changes,which is central to tuning,engine development and performance engineering work.