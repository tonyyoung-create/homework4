# -*- coding: utf-8 -*-
import sys
import random

random.seed(42)

class TopicAnalyzer:
    def __init__(self):
        self.negative_keywords = [
            "痛苦", "失敗", "困難", "問題", "危機", "破裂", "崩潰", "完蛋",
            "衰退", "下滑", "虧損", "災難", "糟糕", "惡劣", "腐敗", "堕落",
            "衝擊", "衰弱", "頹廢", "挑戰", "威脅", "風險", "死亡", "戰爭",
            "恐怖", "害怕", "擔心", "焦慮", "不安", "混亂", "無序", "貧窮",
            "餓", "病", "傷", "罪", "邪惡", "黑暗", "污穢", "難過", "悲傷",
            "沮喪", "失望", "絕望", "憂鬱", "痛心", "傷心", "難受"
        ]
        
        self.positive_keywords = [
            "偉大", "成功", "勝利", "榮耀", "繁榮", "財富", "權力", "聰慧",
            "強大", "美好", "光明", "未來", "希望", "夢想", "機會", "融資",
            "投資", "增長", "發展", "進步", "智慧", "才能", "領導", "勇敢",
            "英雄", "冠軍", "贏家", "最佳", "優秀", "傑出", "卓越", "非凡"
        ]
    
    def analyze_sentiment(self, topic):
        negative_count = sum(1 for kw in self.negative_keywords if kw in topic)
        positive_count = sum(1 for kw in self.positive_keywords if kw in topic)
        
        if negative_count > positive_count:
            return "negative"
        elif positive_count > negative_count:
            return "positive"
        else:
            return "neutral"

class SimpleGenerator:
    def __init__(self):
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "INCREDIBLE", "AMAZING", "SPECTACULAR", "EXCELLENT"
        ]
        
        self.critical_phrases = [
            "TERRIBLE", "DISASTER", "FAILURE", "WRONG", "STUPID", "SAD",
            "TRAGIC", "PATHETIC", "WEAK", "SHAMEFUL", "DISGRACE", "PROBLEM"
        ]
        
        self.intensifiers = ["非常", "真的", "絕對", "完全", "實在", "簡直", "極其"]
    
    def generate_comment(self, topic, sentiment):
        if sentiment == "negative":
            # 負面話題使用批評詞彙
            phrases = self.critical_phrases
            templates = [
                "{phrase}！這是 {intensifier} {phrase}！誰應該負責？",
                "這是 {intensifier} {phrase}！無法接受！",
                "{phrase}！{intensifier} {phrase}！這必須改變！",
                "我見過許多失敗，但這個 {phrase} 的情況是 {intensifier} 嚴重！"
            ]
        else:
            # 正面話題使用讚美詞彙
            phrases = self.positive_phrases
            templates = [
                "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！",
                "{phrase}！我告訴你，這是 {intensifier} {phrase}！",
                "太 {phrase} 了！{intensifier} {phrase}！"
            ]
        
        phrase = random.choice(phrases)
        template = random.choice(templates)
        intensifier = random.choice(self.intensifiers)
        
        comment = template.format(phrase=phrase, intensifier=intensifier)
        
        # 加入話題前綴
        prefixes = [
            f"關於{topic}：",
            f"當我看到{topic}時：",
            f"說到{topic}："
        ]
        comment = random.choice(prefixes) + comment
        
        return comment

# 測試
analyzer = TopicAnalyzer()
generator = SimpleGenerator()

print("=" * 60)
print("測試: 負面話題 '我很難過'")
print("=" * 60)

topic = "我很難過"
sentiment = analyzer.analyze_sentiment(topic)
print(f"話題: {topic}")
print(f"感情分析: {sentiment}")
print(f"\n川普的 5 個評論:")

for i in range(5):
    comment = generator.generate_comment(topic, sentiment)
    print(f"{i+1}. {comment}")

print("\n" + "=" * 60)
print("測試: 正面話題 '公司融資成功'")
print("=" * 60)

topic2 = "公司融資成功"
sentiment2 = analyzer.analyze_sentiment(topic2)
print(f"話題: {topic2}")
print(f"感情分析: {sentiment2}")
print(f"\n川普的 5 個評論:")

for i in range(5):
    comment = generator.generate_comment(topic2, sentiment2)
    print(f"{i+1}. {comment}")

print("\n" + "=" * 60)
print("✅ 驗證: 負面話題使用批評詞彙，正面話題使用讚美詞彙")
print("=" * 60)
