"""An example of operating the ECSimpleSnow model through PyMT."""

from pymt.models import ECSimpleSnow


# Instantiate the model and get its name.
m = ECSimpleSnow()
print(m.name)

# List input and output variable names.
print("Input variable names:")
for name in m.input_var_names:
    print(" - {}".format(name))
print("Output variable names:")
for name in m.output_var_names:
    print(" - {}".format(name))

# Call setup to get default config and data files.
defaults = m.setup(".")

# Initialize the model with the defaults.
m.initialize(*defaults)

# Display the start, end, and current model time.
print("Start time: {}".format(m.start_time))
print("End time: {}".format(m.end_time))
print("Current time: {}".format(m.time))

# Update the model state.
print("Update the model state...")
m.update()
print("Current time: {}".format(m.time))

# Get the snow depth at this time.
depth = m.var["snowpack__depth"].data
units = m.var["snowpack__depth"].units
print("Snow depth: {} {}".format(depth, units))

# Advance the model to the end.
print("Run the model to the end...")
m.update_until(m.end_time)
print("Current time: {}".format(m.time))

# Get the final snow depth.
depth = m.var["snowpack__depth"].data
units = m.var["snowpack__depth"].units
print("Snow depth: {} {}".format(depth, units))

# Finalize the model.
m.finalize()
