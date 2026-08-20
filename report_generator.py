def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title
        self.sections = []

    @classmethod
    def from_dict(cls, data: dict):
        report = cls(data["title"])
        for title, content in data.get("sections", {}).items():
            report(title, content) 
        return report

    def __call__(self, section_title: str, content: str):
        self.sections.append((section_title, content))

    def __str__(self) -> str:
        out = [f"=== {self.title} ==="]
        for title, body in self.sections:
            out.append(f"\n[{title}]\n{body}")
        return "\n".join(out)

    @uppercase
    def render_headline(self) -> str:
        return f"Report: {self.title}"





report = Report("Monthly Sales")
report("Overview", "Revenue grew by 10%.")  
report("Details", "Top product: Widget A.")

print(report.render_headline())  
print(report)                   

data = {"title": "Quick Audit", "sections": {"Status": "Passed", "Score": "98%"}}
json_report = Report.from_dict(data)
print(json_report)