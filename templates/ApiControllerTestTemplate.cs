using System;
using AdminApi.Controllers.<#package#>;
using <#package#>;
using Moq;
using Xunit;

namespace UnitTests.Controllers.<#package#>
{
    public class <#name#>ApiControllerTests : IDisposable
    {
        private readonly MockRepository _mockRepository;

        private readonly Mock<I<#packageFLUC#>> _mockErp;

        public <#name#>ApiControllerTests()
        {
            _mockRepository = new MockRepository(MockBehavior.Strict);
            _mockErp = _mockRepository.Create<I<#packageFLUC#>>();
        }

        public void Dispose()
        {
            _mockRepository.VerifyAll();
        }

        private <#name#>ApiController Create<#name#>ApiController()
        {
            return new <#name#>ApiController(_mockErp.Object);
        }
    }
}