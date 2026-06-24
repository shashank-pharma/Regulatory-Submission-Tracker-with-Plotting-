# %%
import os

print(os.listdir())

# %%
import os

print(os.getcwd())

# %%
import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("drug_submmision.xlsx")
df = pd.DataFrame(df)

df.columns = df.columns.str.strip()
df["Status"] = df["Status"].str.strip()

print(df.columns)
df["Submitted"] = pd.to_datetime(df["Submitted"])
df["Deadline"]  = pd.to_datetime(df["Deadline"])

print("=" * 60)
print("  REGULATORY SUBMISSION TRACKER")
print("=" * 60)
print(df[["Drug","Agency","Type","Status","Deadline"]]
      .to_string(index=False))

status_count = df["Status"].value_counts()
print("\n--- Status Count ---")
print(status_count)

pending = df[df["Status"] == "Pending"].sort_values("Deadline")
print(f"\n--- Pending Submissions ({len(pending)}) ---")
print(pending[["Drug","Agency","Deadline"]].to_string(index=False))

df["Days_Remaining"] = (
    df["Deadline"] - pd.Timestamp("today")
).dt.days

df["Priority"] = df["Days_Remaining"].apply(
    lambda x: "!!!! URGENT" if x < 180 else " OK"
)

print(f"\n--- Deadline Urgency ---")
print(df[["Drug","Status","Days_Remaining","Priority"]]
      .sort_values("Days_Remaining")
      .to_string(index=False))

colors_pie = ["#2e7d32","#f57f17","#d32f2f","#1565c0"]
plt.figure(figsize=(7, 6))
plt.pie(
    status_count.values,
    labels=status_count.index,
    autopct="%1.0f%%",
    colors=colors_pie,
    startangle=140,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
)
plt.title("Regulatory Submission Status Breakdown\n"
          "CDSCO + FDA Combined",
          fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("submission_status.png", dpi=150,
            bbox_inches="tight")
plt.show()
print("✅ submission_status.png saved")

# ── 6. AGENCY BAR CHART ──────────────────────────────
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Agency",
              palette=["#1565c0","#d32f2f"],
              order=["CDSCO","FDA"])
plt.title("Submissions by Agency",
          fontsize=13, fontweight="bold")
plt.xlabel("Regulatory Agency", fontsize=12)
plt.ylabel("Number of Submissions", fontsize=12)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("agency_chart.png", dpi=150,
            bbox_inches="tight")
plt.show()
print("✅ agency_chart.png saved")




