"""
測試 app_cloud_only_v2.py - 話題感知系統
測試話題：負面（美國完蛋了）和正面（公司融資成功）
"""

import random
import sys

class TopicAnalyzer:
    """話題分析器 - 檢測話題的正負性"""
    
    def __init__(self):
        """初始化話題分析器"""
        self.negative_keywords = [
            "痛苦", "失敗", "困難", "問題", "危機", "破裂", "崩潰", "完蛋",
            "衰退", "下滑", "虧損", "災難", "糟糕", "惡劣", "腐敗", "堕落",
            "衝擊", "衰弱", "頹廢", "挑戰", "威脅", "風險", "死亡", "戰爭"
        ]
        
        self.positive_keywords = [
            "偉大", "成功", "勝利", "榮耀", "繁榮", "財富", "權力", "聰慧",
            "強大", "美好", "光明", "未來", "希望", "夢想", "機會", "融資",
            "投資", "增長", "發展", "進步", "智慧", "才能", "領導", "勇敢"
        ]
    
    def analyze_sentiment(self, topic: str) -> str:
        """分析話題的正負性"""
        topic_lower = topic.lower()
        
        negative_count = sum(1 for kw in self.negative_keywords if kw in topic_lower)
        positive_count = sum(1 for kw in self.positive_keywords if kw in topic_lower)
        
        if negative_count > positive_count:
            return "negative"
        elif positive_count > negative_count:
            return "positive"
        else:
            return "neutral"


class TrumpCommentGenerator:
    """川普風格評論生成器 - 話題感知版本"""
    
    def __init__(self):
        """初始化生成器"""
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "INCREDIBLE", "AMAZING", "SPECTACULAR", "EXCELLENT"
        ]
        
        self.critical_phrases = [
            "TERRIBLE", "DISASTER", "FAILURE", "WRONG", "STUPID", "SAD",
            "TRAGIC", "PATHETIC", "WEAK", "SHAMEFUL", "DISGRACE", "PROBLEM"
        ]
        
        self.intensifiers = [
            "非常", "真的", "絕對", "完全", "實在", "簡直", "極其"
        ]
        
        self.superlatives = [
            "最", "最最", "絕對是", "真的是", "我見過的最"
        ]
        
        # 負面話題的評論範本
        self.negative_comment_templates_critical = [
            "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！誰應該負責？",
            "{phrase}！我告訴你，這是 {intensifier} {phrase} 的！簡直無法接受！",
            "太 {phrase} 了！如果不立即改變，會發生什麼？",
            "這是我見過 {superlative} {phrase} 的事情！真的，{intensifier} {phrase}！必須改變！",
            "{phrase}！{intensifier} {phrase}！{intensifier} {phrase}！這不能再繼續了！"
        ]
        
        self.negative_comment_templates_analysis = [
            "我知道 {phrase} 的事物什麼樣子。這？這是 {phrase}！非常 {phrase}！這是對人民的背叛！",
            "許多人看不到，但這 - 這是 {intensifier} {phrase}！我看得很清楚！",
            "你知道我見過什麼？失敗。這就是失敗。這是 {intensifier} {phrase}！",
            "我做過許多事，見過許多事。這？這是 {intensifier} {phrase} 的。非常非常錯誤！"
        ]
        
        self.negative_comment_templates_blame = [
            "誰造成了這個 {phrase}？誰該負責？必須有人承擔責任！",
            "這個 {phrase} 的情況是媒體和失敗者製造的。我會改變這一切！",
            "許多 {phrase} 的政客造成了這個混亂。不再容許！",
            "如果我早一點掌權，這個 {phrase} 的局面永遠不會發生！"
        ]
        
        self.negative_comment_templates_promise = [
            "這個 {phrase} 的情況在我手下絕不會發生。我會改變一切！",
            "別擔心，這個 {phrase} 的問題很容易解決。相信我！",
            "聽我說，我會把這從 {phrase} 變成 GREAT。百分之百！",
            "這個 {phrase} 的局面？我會扭轉它。沒有人能比我做得更好！"
        ]
        
        # 負面話題的最終回應
        self.negative_final_templates_critical = [
            "這個 {phrase} 的局面必須改變！我會做得更好。相信我！- 川普",
            "這是 {intensifier} {phrase}！但別擔心，我會解決它。沒有人能比我做得更好！- 川普"
        ]
        
        self.negative_final_templates_promise = [
            "我見過許多 {phrase} 的情況，但我知道如何修復它。相信我，我會改變一切！- 川普",
            "這個 {phrase} 的問題？在我的領導下，會成為 GREAT。百分百！- 川普"
        ]
        
        self.negative_final_templates_action = [
            "足夠了！這個 {phrase} 的情況必須立即改變。我會採取行動！- 川普",
            "{phrase}！不再容許！我會讓一切恢復 GREAT。相信川普！- 川普"
        ]
        
        self.topic_analyzer = TopicAnalyzer()
    
    def generate_comment(self, topic: str, sentiment: str) -> str:
        """生成單個評論 - 基於話題的正負性"""
        
        if sentiment == "negative":
            comment_style = random.choice(['critical', 'analysis', 'blame', 'promise'])
            
            if comment_style == 'critical':
                template = random.choice(self.negative_comment_templates_critical)
            elif comment_style == 'analysis':
                template = random.choice(self.negative_comment_templates_analysis)
            elif comment_style == 'blame':
                template = random.choice(self.negative_comment_templates_blame)
            else:
                template = random.choice(self.negative_comment_templates_promise)
            
            phrase = random.choice(self.critical_phrases)
        else:
            # 簡化的正面範本
            templates = [
                "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！",
                "{phrase}！我告訴你，這是 {intensifier} {phrase} 的！",
                "太 {phrase} 了！",
                "我見過好，但這是 {intensifier} {superlative} {phrase}！",
            ]
            template = random.choice(templates)
            phrase = random.choice(self.positive_phrases)
        
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        comment = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        if random.random() > 0.4:
            prefixes = [f"關於{topic}：", f"當我看到{topic}時：", f"說到{topic}：", f"這個{topic}？"]
            comment = random.choice(prefixes) + comment
        
        return comment
    
    def generate_five_comments(self, topic: str, sentiment: str) -> list:
        """生成 5 個評論"""
        comments = []
        
        for i in range(5):
            comment = self.generate_comment(topic, sentiment)
            comments.append(comment)
        
        return comments
    
    def generate_final_response(self, topic: str, sentiment: str) -> str:
        """生成最終回應 - 基於話題的正負性"""
        
        if sentiment == "negative":
            response_style = random.choice(['critical', 'promise', 'action'])
            
            if response_style == 'critical':
                template = random.choice(self.negative_final_templates_critical)
            elif response_style == 'promise':
                template = random.choice(self.negative_final_templates_promise)
            else:
                template = random.choice(self.negative_final_templates_action)
            
            phrase = random.choice(self.critical_phrases)
        else:
            templates = [
                "這是 {phrase}！完全 {phrase}！- 川普",
                "這會成為 {superlative} 大的 {phrase} 故事！- 川普",
            ]
            template = random.choice(templates)
            phrase = random.choice(self.positive_phrases)
        
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        response = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        return response
    
    def generate(self, topic: str):
        """完整的生成過程"""
        sentiment = self.topic_analyzer.analyze_sentiment(topic)
        comments = self.generate_five_comments(topic, sentiment)
        final_response = self.generate_final_response(topic, sentiment)
        
        return {
            "topic": topic,
            "sentiment": sentiment,
            "comments": comments,
            "final_response": final_response
        }


def main():
    """主測試函數"""
    print("=" * 80)
    print("🎤 川普評論生成器 - 話題感知系統測試")
    print("=" * 80)
    print()
    
    generator = TrumpCommentGenerator()
    
    # 測試 1：負面話題
    print("🔴 測試 1：負面話題")
    print("=" * 80)
    topic1 = "美國完蛋了"
    print(f"📌 話題：{topic1}\n")
    
    result1 = generator.generate(topic1)
    print(f"📊 分析結果：{'❌ 負面話題' if result1['sentiment'] == 'negative' else '✅ 正面話題'}\n")
    
    print("川普的 5 個評論：")
    for i, comment in enumerate(result1["comments"], 1):
        print(f"{i}. {comment}\n")
    
    print(f"川普的最終回應：\n{result1['final_response']}\n")
    
    print("\n" + "=" * 80)
    
    # 測試 2：正面話題
    print("\n🟢 測試 2：正面話題")
    print("=" * 80)
    topic2 = "公司融資成功"
    print(f"📌 話題：{topic2}\n")
    
    result2 = generator.generate(topic2)
    print(f"📊 分析結果：{'❌ 負面話題' if result2['sentiment'] == 'negative' else '✅ 正面話題'}\n")
    
    print("川普的 5 個評論：")
    for i, comment in enumerate(result2["comments"], 1):
        print(f"{i}. {comment}\n")
    
    print(f"川普的最終回應：\n{result2['final_response']}\n")
    
    print("\n" + "=" * 80)
    print("✅ 測試完成！")
    print("=" * 80)
    print("\n📝 分析結果：")
    print("- 負面話題應該使用批評、同情、責任追究的風格")
    print("- 正面話題應該使用讚美、鼓勵的風格")
    print("- 每個話題都能調整回應方式，提高相關性")


if __name__ == "__main__":
    main()
