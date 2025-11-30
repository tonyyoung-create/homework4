"""
測試改進的川普評論生成器 - 展示多樣性
"""

import random
import sys

# 簡單的生成器實現（不需要 Streamlit）
class TrumpCommentGeneratorTest:
    """川普風格評論生成器 - 測試版本"""
    
    def __init__(self):
        """初始化生成器"""
        # 擴展短語庫 - 各種強度和類型
        self.positive_phrases = [
            "GREAT", "FANTASTIC", "TREMENDOUS", "BEAUTIFUL", "MAGNIFICENT",
            "WONDERFUL", "FANTASTIC", "INCREDIBLE", "AMAZING", "SPECTACULAR"
        ]
        
        self.intensifiers = [
            "非常", "真的", "絕對", "完全", "實在", "簡直", "極其"
        ]
        
        # 多樣化的評論範本 - 不同的句式結構
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
            "人們總是說好，但 {phrase}？這是另一個等級的 {phrase}！",
            "我見過好，但這是 {intensifier} {superlative} {phrase}！",
            "不，不，不 - 我說的是 {intensifier} {phrase}，而這正是！"
        ]
        
        self.comment_templates_emphatic = [
            "讓我告訴你 - {phrase}！完全 {phrase}！非常 {phrase}！",
            "這就是我想說的一切：{phrase}！{intensifier} {phrase}！就是這樣！",
            "我能想到的只有一個詞：{phrase}！{intensifier} {phrase}！",
            "{phrase}。{phrase}。{intensifier} {phrase}。這就是全部！"
        ]
        
        self.superlatives = [
            "最", "最最", "絕對是", "真的是", "我見過的最"
        ]
    
    def generate_comment(self, topic: str) -> str:
        """生成單個評論 - 使用多樣化的方法"""
        # 隨機選擇評論風格
        comment_style = random.choice([
            'basic', 'analytical', 'comparison', 'emphatic'
        ])
        
        if comment_style == 'basic':
            template = random.choice(self.comment_templates_basic)
        elif comment_style == 'analytical':
            template = random.choice(self.comment_templates_analytical)
        elif comment_style == 'comparison':
            template = random.choice(self.comment_templates_comparison)
        else:  # emphatic
            template = random.choice(self.comment_templates_emphatic)
        
        # 隨機選擇填充詞
        phrase = random.choice(self.positive_phrases)
        intensifier = random.choice(self.intensifiers)
        superlative = random.choice(self.superlatives)
        
        # 格式化評論
        comment = template.format(
            phrase=phrase,
            intensifier=intensifier,
            superlative=superlative
        )
        
        # 可選地添加話題前綴
        if random.random() > 0.4:
            prefixes = [
                f"關於{topic}：",
                f"當我看到{topic}時：",
                f"說到{topic}：",
                f"這個{topic}？"
            ]
            comment = random.choice(prefixes) + comment
        
        return comment


def main():
    """測試主函數"""
    print("=" * 80)
    print("🎤 川普評論生成器 - 多樣性測試")
    print("=" * 80)
    
    topic = "我的新公司融資"
    generator = TrumpCommentGeneratorTest()
    
    print(f"\n📌 話題：{topic}\n")
    
    # 測試 3 次 5 個評論，展示多樣性
    for batch in range(3):
        print(f"\n🔄 第 {batch + 1} 輪 - 生成 5 個評論：")
        print("-" * 80)
        
        comments = []
        for i in range(5):
            comment = generator.generate_comment(topic)
            comments.append(comment)
            print(f"{i+1}. {comment}\n")
        
        if batch < 2:
            print("\n" + "=" * 80)
            print("⏳ 下一輪...\n")
    
    print("=" * 80)
    print("✅ 測試完成！")
    print("=" * 80)
    print("\n📝 說明：")
    print("- 每個評論都使用不同的句式結構")
    print("- 包含隨機選擇的強度詞和比較詞")
    print("- 會根據機率添加話題前綴")
    print("- 不同輪次的評論應該有明顯的多樣性")
    print("\n✅ 與原版本相比，新版本提供了更多的多樣化和創意性！")


if __name__ == "__main__":
    main()
