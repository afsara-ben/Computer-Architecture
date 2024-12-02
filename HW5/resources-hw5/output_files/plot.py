import matplotlib.pyplot as plt

# Data for the graph
cache_designs = ['Direct Mapped', '4-Way SA', '8-Way SA', '16-Way SA','32-Way SA']
CPI_stall = [150.7239174,
150.7239174,
150.7239174,
150.7239174,
150.7239174]  # Example CPI stall values

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(cache_designs, CPI_stall, alpha=0.7)
# plt.bar(cache_designs, CPI_stall, edgecolor='black', alpha=0.7)
# bars = plt.bar(cache_designs, CPI_stall, edgecolor='black', alpha=0.7)
#
# # Add text labels above the bars
# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
#              f"{round(bar.get_height())}", ha='center', va='bottom', fontsize=10)

plt.xlabel('Cache Designs', fontsize=12)
plt.ylabel('CPI Stall', fontsize=12)
# plt.ylim(bottom=40, top=120)
plt.title('CPI Stall vs Cache Designs (block_size=64)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the graph
plt.show()
