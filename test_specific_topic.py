"""
測試 app_cloud_only.py - 模擬用户输入"美国人很痛苦"
验证输出是否多样化或是制式化
"""

import random
import sys

# 复制 app_cloud_only.py 中的 TrumpCommentGenerator 类
class TrumpCommentGenerator:
    """川普風格評論生成器 - 增強版本，更多樣化的生成"""
    
    def __init__(self):
        """初始化生成器"""
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "FANTASTIC", "INCREDIBLE", "AMAZING", "SPECTACULAR"
        ]
        
        self.intensifiers = [
            "非常", "真的", "絕對", "完全", "實在", "簡直", "極其"
        ]
        
        self.affirm_phrases = [
            "VERY SMART", "VERY STRONG", "VERY GOOD", "VERY WISE", "VERY SHARP",
            "VERY SMART MOVE", "VERY EXCELLENT CHOICE", "VERY WELL DONE"
        ]
        
        self.superlatives = [
            "最", "最最", "絕對是", "真的是", "我見過的最"
        ]
        
        self.comment_templates_basic = [
            "這是 {intensifier} {phrase} 的！真的，{intensifier} {phrase}！",
            "{phrase}！我告訴你，這是 {intensifier} {phrase} 的！",
            "太 {phrase} 了！如果我沒親眼看到，我都不相信會這麼 {phrase}！",
            "這是我見過 {superlative} {phrase} 的事情！真的，{intensifier} {phrase}！",
            "{phrase}！{intensifier} {phrase}！{intensifier} {phrase}！"
        ]
        
        self.comment_templates_analytical = [
            "我知道 {phrase} 的事物什麼樣子。這？這是 {phrase}！非常 {phrase}！",
            "許多人說 {phrase}，但這 - 這是 {intensifier} {phrase}！",
            "你知道我見過什麼？失敗。但這不是。這是 {intensifier} {phrase}！",
            "我做過許多事，見過許多事。這？這是 {intensifier} {phrase} 的。相信我！"
        ]
        
        self.comment_templates_comparison = [
            "比起其他我見過的，這是 {superlative} {phrase} 的。{intensifier} {phrase}！",
            "人們總是說 {phrase}，但這 - 這是另一個等級的 {phrase}！",
            "我見過好，但這是 {intensifier} {superlative} {phrase}！",
            "不，不，不 - 我說的是 {intensifier} {phrase}，而這正是！"
        ]
        
        self.comment_templates_emphatic = [
            "讓我告訴你 - {phrase}！完全 {phrase}！非常 {phrase}！",
            "這就是我想說的一切：{phrase}！{intensifier} {phrase}！就是這樣！",
            "我能想到的只有一個詞：{phrase}！{intensifier} {phrase}！",
            "{phrase}。{phrase}。{intensifier} {phrase}。這就是全部！"
        ]
        
        self.final_templates_strong = [
            "讓我告訴你，這真的是 {phrase} 的！我見過很多，但這是 {superlative} 最 {phrase} 的。這是個 {intensifier} {phrase} 的決定。我知道成功，而這就是 {phrase}！- 川普",
            "這是 {phrase}！完全 {phrase}！我可以告訴你，這會成為 {intensifier} {phrase} 的成功故事。相信我！- 川普"
        ]
        
        self.final_templates_modest = [
            "我很少給出 {phrase} 的評價，但這次我必須說 - 這真的是 {phrase}！做得 {intensifier} 好！- 川普",
            "通常我對這種事很挑剔，但這？這是 {intensifier} {phrase}！非常好的工作！- 川普"
        ]
        
        self.final_templates_rhetorical = [
            "{phrase}！這就是我想說的 - 完全 {phrase}！這會成為 {superlative} 大的 {phrase} 故事之一！- 川普",
            "你知道什麼是真正 {phrase} 的嗎？這個！這就是 {intensifier} {phrase}！最好的！- 川普"
        ]
    
    def generate_comment(self, topic: str) -> str:
        """生成單個評論 - 使用多樣化的方法"""
        comment_style = random.choice([
            'basic', 'analytical', 'comparison', 'emphatic'
        ])
        
        if comment_style == 'basic':
            template = random.choice(self.comment_templates_basic)
        elif comment_style == 'analytical':
            template = random.choice(self.comment_templates_analytical)
        elif comment_style == 'comparison':
            template = random.choice(self.comment_templates_comparison)
        else:
            template = random.choice(self.comment_templates_emphatic)
        
        phrase = random.choice(self.positive_phrases)
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        comment = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        if random.random() > 0.4:
            prefixes = [
                f"關於{topic}：",
                f"當我看到{topic}時：",
                f"說到{topic}：",
                f"這個{topic}？"
            ]
            comment = random.choice(prefixes) + comment
        
        return comment
    
    def generate_five_comments(self, topic: str) -> list:
        """生成 5 個評論"""
        comments = []
        
        print(f"⏳ 生成 {topic} 的 5 個評論...\n")
        
        for i in range(5):
            comment = self.generate_comment(topic)
            comments.append(comment)
            print(f"{i+1}. {comment}\n")
        
        return comments
    
    def generate_final_response(self, topic: str, comments: list) -> str:
        """生成最終回應 - 使用多樣的範本"""
        response_style = random.choice(['strong', 'modest', 'rhetorical'])
        
        if response_style == 'strong':
            template = random.choice(self.final_templates_strong)
        elif response_style == 'modest':
            template = random.choice(self.final_templates_modest)
        else:
            template = random.choice(self.final_templates_rhetorical)
        
        phrase = random.choice(self.positive_phrases)
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        response = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        return response


def main():
    """主測試函數"""
    print("=" * 80)
    print("🎤 川普評論生成器 - 話題測試")
    print("=" * 80)
    print()
    
    topic = "美國人很痛苦"
    generator = TrumpCommentGenerator()
    
    # 測試 5 次，看看每次的輸出是否不同
    print(f"📌 話題：{topic}\n")
    print("=" * 80)
    print("🧪 測試 5 次生成結果，驗證多樣性\n")
    
    for test_round in range(5):
        print(f"\n🔄 第 {test_round + 1} 次生成：")
        print("-" * 80)
        
        comments = generator.generate_five_comments(topic)
        final_response = generator.generate_final_response(topic, comments)
        
        print(f"川普的最終回應：")
        print(final_response)
        print()
        
        if test_round < 4:
            print("=" * 80)
    
    print("\n" + "=" * 80)
    print("✅ 測試完成！")
    print("=" * 80)
    print("\n📝 分析結果：")
    print("- 每次點擊「讓川普說話」，都應該看到不同的評論和回應")
    print("- 如果所有結果都相同 → 表示仍然是制式化問題")
    print("- 如果每次都不同 → 表示多樣化改進成功")


if __name__ == "__main__":
    main()
